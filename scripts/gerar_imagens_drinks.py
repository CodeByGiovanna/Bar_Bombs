"""Gera imagens estilizadas para os drinks sem foto."""
from PIL import Image, ImageDraw, ImageFont
import os, json, math

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'static', 'images', 'drinks')
DATA_FILE  = os.path.join(os.path.dirname(__file__), '..', 'data', 'drinks.json')

DRINKS_SEM_FOTO = [
    {"slug": "pina-colada",            "nome": "Piña Colada",            "cor": (255, 200, 60),  "cor2": (255, 140, 20)},
    {"slug": "mango-tango",            "nome": "Mango Tango",            "cor": (255, 140, 20),  "cor2": (230, 80,  10)},
    {"slug": "passion-fruit-daiquiri", "nome": "Passion Fruit\nDaiquiri","cor": (200, 80,  200), "cor2": (140, 20, 160)},
    {"slug": "watermelon-cooler",      "nome": "Watermelon Cooler",      "cor": (240, 60,  80),  "cor2": (180, 20,  60)},
    {"slug": "strawberry-basil-smash", "nome": "Strawberry\nBasil Smash","cor": (220, 40,  70),  "cor2": (160, 20,  50)},
    {"slug": "mai-tai",                "nome": "Mai Tai",                "cor": (255, 160, 30),  "cor2": (200, 80,  10)},
    {"slug": "zombie",                 "nome": "Zombie",                 "cor": (200, 30,  30),  "cor2": (100, 10,  10)},
    {"slug": "dark-stormy",            "nome": "Dark & Stormy",          "cor": (160, 90,  20),  "cor2": (80,  40,  10)},
    {"slug": "coco-loco",              "nome": "Coco Loco",              "cor": (60,  200, 200), "cor2": (20, 130, 160)},
    {"slug": "brazilian-sunset",       "nome": "Brazilian Sunset",       "cor": (255, 100, 30),  "cor2": (220, 30,  100)},
    {"slug": "lychee-martini",         "nome": "Lychee Martini",         "cor": (240, 140, 180), "cor2": (180, 60,  140)},
    {"slug": "thai-basil-smash",       "nome": "Thai Basil Smash",       "cor": (60,  200, 80),  "cor2": (20,  120, 40)},
    {"slug": "blue-lagoon-tropical",   "nome": "Blue Lagoon\nTropical",  "cor": (40,  160, 255), "cor2": (10,  80,  200)},
    {"slug": "tamarind-sour",          "nome": "Tamarind Sour",          "cor": (180, 110, 40),  "cor2": (120, 60,  10)},
    {"slug": "hibiscus-fizz",          "nome": "Hibiscus Fizz",          "cor": (220, 40,  160), "cor2": (160, 10,  100)},
]

SIZE = 800


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def gerar(drink):
    img = Image.new('RGB', (SIZE, SIZE), (0, 20, 8))
    draw = ImageDraw.Draw(img, 'RGBA')

    # Fundo degradê diagonal
    for y in range(SIZE):
        t = y / SIZE
        bg = lerp_color((0, 26, 10), (0, 10, 4), t)
        draw.line([(0, y), (SIZE, y)], fill=bg)

    # Brilho radial central (camadas concêntricas)
    cx, cy = SIZE // 2, SIZE // 2 - 40
    cor_princ = drink['cor']
    for r in range(300, 0, -4):
        alpha = int(120 * (r / 300) ** 0.6)
        t = r / 300
        c = lerp_color(cor_princ, (0, 26, 10), t)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*c, alpha))

    # Silhueta do copo (triângulo invertido + haste + base)
    glass_color = (*lerp_color(cor_princ, (255, 255, 255), 0.5), 220)
    gx, gy = cx, cy
    w, h = 120, 110
    # taça (triângulo invertido)
    draw.polygon([
        (gx - w, gy - h),
        (gx + w, gy - h),
        (gx,     gy + 30),
    ], fill=(*cor_princ, 60), outline=glass_color)
    # haste
    draw.rectangle([gx - 6, gy + 30, gx + 6, gy + 80], fill=glass_color)
    # base
    draw.rectangle([gx - 55, gy + 80, gx + 55, gy + 92], fill=glass_color)

    # Brilho na borda superior do copo
    highlight = (*lerp_color(cor_princ, (255, 255, 255), 0.8), 180)
    draw.ellipse([gx - w, gy - h - 8, gx - w + 40, gy - h + 8], fill=highlight)

    # Linha decorativa
    line_y = SIZE - 140
    draw.line([(80, line_y), (SIZE - 80, line_y)], fill=(*cor_princ, 120), width=1)

    # Nome do drink
    nome_lines = drink['nome'].split('\n')
    font_size = 68 if len(nome_lines) == 1 else 56
    try:
        font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', font_size)
        font_small = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 26)
    except Exception:
        font = ImageFont.load_default()
        font_small = font

    text_y = SIZE - 120
    for line in nome_lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        # sombra
        draw.text(((SIZE - tw) // 2 + 2, text_y + 2), line, font=font, fill=(0, 0, 0, 180))
        # texto principal
        draw.text(((SIZE - tw) // 2, text_y), line, font=font, fill=(*lerp_color(cor_princ, (255,255,255), 0.7), 255))
        text_y += font_size + 6

    # Marca d'água
    marca = "BOMBS BAR"
    bbox = draw.textbbox((0, 0), marca, font=font_small)
    tw = bbox[2] - bbox[0]
    draw.text(((SIZE - tw) // 2, SIZE - 38), marca, font=font_small, fill=(*cor_princ, 80))

    filename = f"{drink['slug'].replace('-', '_')}.jpg"
    path = os.path.join(OUTPUT_DIR, filename)
    img.convert('RGB').save(path, 'JPEG', quality=90)
    print(f"  ✓  {filename}")
    return f"images/drinks/{filename}"


def atualizar_json(mapa_slug_imagem):
    with open(DATA_FILE, encoding='utf-8') as f:
        drinks = json.load(f)
    for d in drinks:
        if d['slug'] in mapa_slug_imagem:
            d['imagem'] = mapa_slug_imagem[d['slug']]
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(drinks, f, ensure_ascii=False, indent=2)
    print(f"\ndrinks.json atualizado com {len(mapa_slug_imagem)} imagens.")


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    mapa = {}
    print("Gerando imagens...\n")
    for drink in DRINKS_SEM_FOTO:
        mapa[drink['slug']] = gerar(drink)
    atualizar_json(mapa)
    print("\nPronto!")
