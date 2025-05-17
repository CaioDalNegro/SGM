from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

consultas = []

@app.route('/')
def index():
    try:
        pacientes = requests.get("http://localhost:5001/api/pacientes").json()
    except:
        pacientes = []
    return render_template('consulta.html', pacientes=pacientes)

@app.route('/api/consultas', methods=['GET'])
def listar_consultas():
    return jsonify(consultas)

@app.route('/api/consultas', methods=['POST'])
def adicionar_consulta():
    dados = request.get_json()
    nome = dados.get('nome_paciente')
    data = dados.get('data')
    hora = dados.get('hora')

    if not nome or not data or not hora:
        return jsonify({'error': 'Dados incompletos'}), 400

    # Verifica se o paciente está cadastrado
    pacientes = requests.get("http://localhost:5001/api/pacientes").json()
    nomes_pacientes = [p['nome'] for p in pacientes]

    if nome not in nomes_pacientes:
        return jsonify({'error': 'Paciente não cadastrado'}), 400

    consulta = {'nome_paciente': nome, 'data': data, 'hora': hora}
    consultas.append(consulta)
    return jsonify({'message': 'Consulta agendada com sucesso'}), 201

if __name__ == '__main__':
    app.run(port=5002)
