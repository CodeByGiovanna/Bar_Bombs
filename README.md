# Bombs Bar 🍸

Site de menu e delivery para o **Bombs Bar** — uma casa de coquetéis tropicais.
Construído com Flask (Python), HTML/CSS/JS puro e integração com o Glovo.

---

## Funcionalidades

- Menu de drinks com cards modernos, preços e animações
- Página de detalhe de cada drink com ingredientes
- Carrinho de pedidos com controle de quantidade
- Integração com a API do Glovo para delivery
- Layout responsivo (mobile-first)
- Navbar fixa com badge do carrinho

---

## Pré-requisitos

- Python 3.10+
- pip

---

## Instalação

```bash
# 1. Clone ou acesse a pasta do projeto
cd Bombs_Bar

# 2. Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

---

## Configuração das variáveis de ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o .env e preencha suas chaves
nano .env
```

| Variável              | Descrição                                      |
|-----------------------|------------------------------------------------|
| `SECRET_KEY`          | Chave secreta do Flask (qualquer string longa) |
| `GLOVO_API_KEY`       | Token da API do Glovo                          |
| `UNSPLASH_ACCESS_KEY` | Token da API do Unsplash (download de imagens) |

> **Nunca** commite o arquivo `.env` com chaves reais. Ele já está no `.gitignore`.

---

## Como rodar localmente

```bash
flask run
```

O site estará disponível em: http://127.0.0.1:5000

---

## Download das imagens (opcional)

Se quiser baixar imagens de alta qualidade via Unsplash:

```bash
# Configure UNSPLASH_ACCESS_KEY no .env primeiro
python scripts/download_images.py
```

---

## Estrutura de pastas

```
Bombs_Bar/
│
├── main.py                      # Arquivo principal Flask
├── requirements.txt             # Dependências
├── README.md                    # Este arquivo
├── .env.example                 # Modelo de variáveis de ambiente
│
├── data/
│   └── drinks.json              # Dados dos drinks (nome, descrição, ingredientes, preço)
│
├── templates/
│   ├── index.html               # Página principal (menu)
│   ├── drink_detail.html        # Página de detalhe do drink
│   └── pedido.html              # Página do carrinho / pedido
│
├── static/
│   ├── css/
│   │   └── style.css            # Estilos principais
│   ├── js/
│   │   └── main.js              # JavaScript (carrinho, toast, interações)
│   └── images/
│       └── drinks/              # Imagens dos drinks
│
├── api/
│   └── glovo_integration.py     # Integração com a API do Glovo
│
├── contatos/
│   └── contato.md               # Informações de contato do bar
│
└── scripts/
    └── download_images.py       # Script para baixar imagens do Unsplash
```

---

## Como adicionar novos drinks

Edite o arquivo `data/drinks.json` e adicione um novo objeto seguindo este modelo:

```json
{
  "nome": "Nome do Drink",
  "slug": "nome-do-drink",
  "descricao_curta": "Frase curta para o card.",
  "descricao": "Descrição completa e apetitosa com 3-4 linhas.",
  "ingredientes": ["Ingrediente 1", "Ingrediente 2", "Ingrediente 3"],
  "preco": 10.50,
  "imagem": "images/drinks/nome_do_drink.jpg"
}
```

Adicione a imagem correspondente em `static/images/drinks/`.
