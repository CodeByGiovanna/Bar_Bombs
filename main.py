from flask import Flask, render_template, session, jsonify, request, redirect, url_for
from dotenv import load_dotenv
import json
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-bombsbar')


def carregar_drinks():
    caminho = os.path.join(os.path.dirname(__file__), 'data', 'drinks.json')
    with open(caminho, encoding='utf-8') as f:
        return json.load(f)


def carregar_petiscos():
    caminho = os.path.join(os.path.dirname(__file__), 'data', 'petiscos.json')
    with open(caminho, encoding='utf-8') as f:
        return json.load(f)


def _total_itens():
    carrinho = session.get('carrinho', [])
    return sum(i['quantidade'] for i in carrinho)


@app.route('/')
def home():
    drinks = carregar_drinks()
    petiscos = carregar_petiscos()
    return render_template('index.html', drinks=drinks, petiscos=petiscos, total_itens=_total_itens())


@app.route('/drink/<slug>')
def detalhe_drink(slug):
    drinks = carregar_drinks()
    drink = next((d for d in drinks if d['slug'] == slug), None)
    if not drink:
        return redirect(url_for('home'))
    return render_template('drink_detail.html', drink=drink, total_itens=_total_itens())


@app.route('/pedido')
def pedido():
    carrinho = session.get('carrinho', [])
    drinks = carregar_drinks()
    petiscos = carregar_petiscos()
    petiscos_itens = [item for cat in petiscos for item in cat['itens']]
    itens = []
    carrinho_valido = []
    total = 0.0
    for item in carrinho:
        produto = next((d for d in drinks if d['nome'] == item['nome']), None)
        if not produto:
            produto = next((p for p in petiscos_itens if p['nome'] == item['nome']), None)
        if produto:
            subtotal = produto['preco'] * item['quantidade']
            itens.append({**produto, 'quantidade': item['quantidade'], 'subtotal': round(subtotal, 2)})
            total += subtotal
            carrinho_valido.append(item)
    # Remove itens obsoletos da sessão para manter badge consistente
    session['carrinho'] = carrinho_valido
    total_itens = sum(i['quantidade'] for i in carrinho_valido)
    return render_template('pedido.html', itens=itens, total=round(total, 2), total_itens=total_itens)


@app.route('/api/carrinho/adicionar', methods=['POST'])
def adicionar_ao_carrinho():
    data = request.get_json()
    nome = data.get('nome', '').strip()
    quantidade = max(1, int(data.get('quantidade', 1)))
    if not nome:
        return jsonify({'sucesso': False, 'mensagem': 'Nome inválido.'}), 400
    carrinho = session.get('carrinho', [])
    item = next((i for i in carrinho if i['nome'] == nome), None)
    if item:
        item['quantidade'] += quantidade
    else:
        carrinho.append({'nome': nome, 'quantidade': quantidade})
    session['carrinho'] = carrinho
    return jsonify({'sucesso': True, 'total_itens': sum(i['quantidade'] for i in carrinho)})


@app.route('/api/carrinho/remover', methods=['POST'])
def remover_do_carrinho():
    data = request.get_json()
    nome = data.get('nome', '').strip()
    carrinho = [i for i in session.get('carrinho', []) if i['nome'] != nome]
    session['carrinho'] = carrinho
    return jsonify({'sucesso': True, 'total_itens': sum(i['quantidade'] for i in carrinho)})


@app.route('/api/carrinho/atualizar', methods=['POST'])
def atualizar_quantidade():
    data = request.get_json()
    nome = data.get('nome', '').strip()
    quantidade = int(data.get('quantidade', 1))
    carrinho = session.get('carrinho', [])
    if quantidade <= 0:
        carrinho = [i for i in carrinho if i['nome'] != nome]
    else:
        item = next((i for i in carrinho if i['nome'] == nome), None)
        if item:
            item['quantidade'] = quantidade
    session['carrinho'] = carrinho
    return jsonify({'sucesso': True, 'total_itens': sum(i['quantidade'] for i in carrinho)})


@app.route('/api/carrinho/limpar', methods=['POST'])
def limpar_carrinho():
    session.pop('carrinho', None)
    return jsonify({'sucesso': True})


if __name__ == '__main__':
    app.run(debug=True)
