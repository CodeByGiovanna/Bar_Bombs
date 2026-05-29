"""
Script para baixar imagens dos drinks via API pública do Unsplash.

Uso:
    python scripts/download_images.py

Requisitos:
    - Criar conta em https://unsplash.com/developers
    - Gerar um Access Key gratuito
    - Definir a variável UNSPLASH_ACCESS_KEY no arquivo .env
"""

import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")
DESTINO = Path(__file__).parent.parent / "static" / "images" / "drinks"

DRINKS = [
    {"nome": "mojito",          "busca": "mojito cocktail drink",          "arquivo": "mojito.jpg"},
    {"nome": "negroni",         "busca": "negroni cocktail drink",         "arquivo": "negroni.jpg"},
    {"nome": "gin tonic",       "busca": "gin tonic cocktail drink",       "arquivo": "gin_tonic.jpg"},
    {"nome": "aperol spritz",   "busca": "aperol spritz cocktail drink",   "arquivo": "aperol_spritz.jpg"},
    {"nome": "moscow mule",     "busca": "moscow mule cocktail drink",     "arquivo": "moscow_mule.jpg"},
    {"nome": "margarita",       "busca": "margarita cocktail drink",       "arquivo": "margarita.jpg"},
    {"nome": "whisky sour",     "busca": "whisky sour cocktail drink",     "arquivo": "whisky_sour.jpg"},
    {"nome": "sex on the beach","busca": "tropical cocktail drink beach",  "arquivo": "sex_on_the_beach.jpg"},
    {"nome": "caipirinha",      "busca": "caipirinha cocktail drink",      "arquivo": "caipirinha.jpg"},
]


def baixar_imagem(busca: str, destino: Path) -> bool:
    url = "https://api.unsplash.com/photos/random"
    params = {"query": busca, "orientation": "landscape"}
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}

    resp = requests.get(url, params=params, headers=headers, timeout=10)
    resp.raise_for_status()

    dados = resp.json()
    img_url = dados["urls"]["regular"]

    img_resp = requests.get(img_url, timeout=15)
    img_resp.raise_for_status()

    destino.write_bytes(img_resp.content)
    return True


def main():
    if not UNSPLASH_ACCESS_KEY:
        print("Erro: variável UNSPLASH_ACCESS_KEY não definida no .env")
        return

    DESTINO.mkdir(parents=True, exist_ok=True)

    for drink in DRINKS:
        caminho = DESTINO / drink["arquivo"]
        if caminho.exists():
            print(f"✓ Já existe: {drink['arquivo']}")
            continue
        print(f"Baixando {drink['nome']}...", end=" ", flush=True)
        try:
            baixar_imagem(drink["busca"], caminho)
            print("OK")
        except Exception as e:
            print(f"ERRO — {e}")


if __name__ == "__main__":
    main()
