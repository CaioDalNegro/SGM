from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # para permitir chamadas do JS
app.static_folder = 'static'

# Simulação de banco de dados
pacientes = []

@app.route('/')
def index():
    return render_template('pacientes.html')

@app.route('/api/pacientes', methods=['GET'])
def listar_pacientes():
    return jsonify(pacientes)

@app.route('/api/pacientes', methods=['POST'])
def cadastrar_paciente():
    data = request.get_json()
    paciente_id = len(pacientes) + 1
    paciente = {
        "id": paciente_id,
        "nome": data.get("nome"),
        "cpf": data.get("cpf"),
        "telefone": data.get("telefone")
    }
    pacientes.append(paciente)
    return jsonify(paciente), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
