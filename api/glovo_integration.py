"""
Integração com a API do Glovo para delivery.

Uso:
    from api.glovo_integration import GlovoClient
    cliente = GlovoClient()
    resultado = cliente.criar_pedido(itens, endereco_entrega)
"""

import os
import requests
from typing import Any


GLOVO_API_BASE = "https://api.glovoapp.com/b2b/orders"


class GlovoClient:
    def __init__(self):
        self.api_key = os.environ.get("GLOVO_API_KEY")
        if not self.api_key:
            raise EnvironmentError(
                "Variável de ambiente GLOVO_API_KEY não definida. "
                "Configure-a no arquivo .env antes de usar."
            )
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def criar_pedido(self, itens: list[dict], endereco_entrega: str) -> dict[str, Any]:
        """
        Cria um pedido de delivery no Glovo.

        Args:
            itens: Lista de dicts com 'nome', 'quantidade' e 'preco'.
            endereco_entrega: Endereço completo para entrega.

        Returns:
            Dict com 'sucesso', 'pedido_id' (se criado) e 'mensagem'.
        """
        payload = {
            "deliveryAddress": endereco_entrega,
            "products": [
                {
                    "name": item["nome"],
                    "quantity": item["quantidade"],
                    "price": item["preco"],
                }
                for item in itens
            ],
        }

        try:
            resposta = requests.post(
                GLOVO_API_BASE,
                json=payload,
                headers=self.headers,
                timeout=10,
            )
            resposta.raise_for_status()
            dados = resposta.json()
            return {
                "sucesso": True,
                "pedido_id": dados.get("orderId"),
                "mensagem": "Pedido criado com sucesso! O entregador está a caminho.",
            }
        except requests.exceptions.HTTPError as e:
            codigo = e.response.status_code if e.response else "?"
            return {
                "sucesso": False,
                "pedido_id": None,
                "mensagem": f"Erro {codigo} ao criar pedido no Glovo. Tente novamente.",
            }
        except requests.exceptions.ConnectionError:
            return {
                "sucesso": False,
                "pedido_id": None,
                "mensagem": "Sem conexão com o Glovo. Verifique sua internet.",
            }
        except requests.exceptions.Timeout:
            return {
                "sucesso": False,
                "pedido_id": None,
                "mensagem": "O Glovo demorou muito para responder. Tente novamente.",
            }

    def verificar_status(self, pedido_id: str) -> dict[str, Any]:
        """
        Verifica o status de um pedido no Glovo.

        Args:
            pedido_id: ID do pedido retornado por criar_pedido().

        Returns:
            Dict com 'sucesso', 'status' e 'mensagem'.
        """
        try:
            resposta = requests.get(
                f"{GLOVO_API_BASE}/{pedido_id}",
                headers=self.headers,
                timeout=10,
            )
            resposta.raise_for_status()
            dados = resposta.json()
            status_map = {
                "PENDING": "Aguardando confirmação",
                "ACCEPTED": "Pedido aceito pelo restaurante",
                "PICKED_UP": "Entregador coletou o pedido",
                "DELIVERED": "Entregue com sucesso!",
                "CANCELLED": "Pedido cancelado",
            }
            status_raw = dados.get("status", "UNKNOWN")
            return {
                "sucesso": True,
                "status": status_map.get(status_raw, status_raw),
                "mensagem": "Status obtido com sucesso.",
            }
        except requests.exceptions.HTTPError as e:
            codigo = e.response.status_code if e.response else "?"
            return {
                "sucesso": False,
                "status": None,
                "mensagem": f"Erro {codigo} ao consultar pedido {pedido_id}.",
            }
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return {
                "sucesso": False,
                "status": None,
                "mensagem": "Não foi possível consultar o status. Verifique sua conexão.",
            }
