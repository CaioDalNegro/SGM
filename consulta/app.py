from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

consultas = []

@app.route('/')
def index():
    return render_template('consulta.html')

@app.route('/api/consultas', methods=['GET'])
def listar_consultas():
    return jsonify(consultas)

@app.route('/api/consultas', methods=['POST'])
def agendar_consulta():
    dados = request.get_json()
    nome_paciente = dados.get('nome_paciente')
    data = dados.get('data')
    hora = dados.get('hora')

    if not nome_paciente or not data or not hora:
        return jsonify({'error': 'Dados incompletos'}), 400

    consulta = {
        'id': len(consultas) + 1,
        'nome_paciente': nome_paciente,
        'data': data,
        'hora': hora
    }
    consultas.append(consulta)
    return jsonify(consulta), 201

if __name__ == '__main__':
    app.run(port=5002, debug=True)
