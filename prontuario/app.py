from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash'

registros = []

CONSULTA_SERVICE_URL = 'http://consulta:5002/api/consultas'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        consulta_id = request.form.get('consulta_id')
        descricao = request.form.get('descricao')

        # Validação básica
        if not consulta_id or not descricao:
            flash('Por favor, preencha todos os campos.', 'error')
            return redirect(url_for('index'))

        try:
            consulta_id_int = int(consulta_id)
        except ValueError:
            flash('O ID da consulta deve ser um número inteiro.', 'error')
            return redirect(url_for('index'))

        # Verificar se a consulta existe via requisição ao serviço de Consulta
        try:
            resposta = requests.get(CONSULTA_SERVICE_URL)
            resposta.raise_for_status()
            consultas = resposta.json()
            consulta = next((c for c in consultas if c['id'] == consulta_id_int), None)

            if not consulta:
                flash(f'Consulta ID {consulta_id_int} não encontrada.', 'error')
                return redirect(url_for('index'))
        except Exception as e:
            flash(f'Erro ao comunicar com o serviço de Consulta: {e}', 'error')
            return redirect(url_for('index'))

        # Criar e armazenar o prontuário localmente
        registro = {
            'id': len(registros) + 1,
            'consulta_id': consulta_id_int,
            'descricao': descricao
        }
        registros.append(registro)

        flash('Prontuário registrado com sucesso!', 'success')
        return redirect(url_for('index'))

    # Se for método GET, renderiza a tela com os registros existentes
    return render_template('prontuario.html', registros=registros)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
