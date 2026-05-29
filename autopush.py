"""
Auto-push: detecta alterações nos arquivos e envia para o GitHub automaticamente.
Uso: python autopush.py
"""

import subprocess
import time
import os
from pathlib import Path

PASTA = Path(__file__).parent
INTERVALO = 10  # segundos entre verificações

IGNORAR = {'.git', '.venv', 'venv', '__pycache__', '.DS_Store', 'autopush.py'}


def estado_arquivos():
    """Retorna um dicionário {arquivo: data_modificação} dos arquivos rastreados."""
    estado = {}
    for caminho in PASTA.rglob('*'):
        partes = caminho.relative_to(PASTA).parts
        if any(p in IGNORAR for p in partes):
            continue
        if caminho.is_file():
            estado[str(caminho)] = caminho.stat().st_mtime
    return estado


def git(cmd):
    return subprocess.run(
        cmd, cwd=str(PASTA), capture_output=True, text=True, shell=True
    )


def push():
    git('git add -A')
    resultado = git('git diff --cached --name-only')
    arquivos = resultado.stdout.strip()
    if not arquivos:
        return

    nomes = arquivos.splitlines()
    descricao = nomes[0] if len(nomes) == 1 else f"{len(nomes)} arquivos alterados"
    git(f'git commit -m "auto: {descricao}"')
    r = git('git push origin main')
    if r.returncode == 0:
        print(f"✅ Push enviado: {descricao}")
    else:
        print(f"❌ Erro no push: {r.stderr.strip()}")


print("👀 Monitorando alterações... (Ctrl+C para parar)")
anterior = estado_arquivos()

while True:
    time.sleep(INTERVALO)
    atual = estado_arquivos()
    if atual != anterior:
        anterior = atual
        push()
