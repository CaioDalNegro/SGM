from flask import Flask, request, jsonify, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash_faturamento'

faturas = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        paciente = request.form.get('paciente')
        valor_servico = request.form.get('valor_servico')

        if not paciente or not valor_servico:
            flash('Por favor, preencha todos os campos.', 'error')
            return redirect(url_for('index'))

        try:
            valor = float(valor_servico)
            if valor < 0:
                raise ValueError('Valor negativo não permitido')
        except ValueError:
            flash('Valor do serviço deve ser um número positivo.', 'error')
            return redirect(url_for('index'))

        # Aqui você pode implementar regras de cálculo de fatura
        # Exemplo: taxa fixa de 10% de imposto
        imposto = valor * 0.10
        valor_total = valor + imposto

        fatura = {
            'id': len(faturas) + 1,
            'paciente': paciente,
            'valor_servico': valor,
            'imposto': round(imposto, 2),
            'valor_total': round(valor_total, 2)
        }
        faturas.append(fatura)

        flash('Fatura criada com sucesso!', 'success')
        return redirect(url_for('index'))

    return render_template('faturamento.html', faturas=faturas)

# API RESTful para listar faturas
@app.route('/api/faturas', methods=['GET'])
def listar_faturas():
    return jsonify(faturas)

# API RESTful para criar fatura via JSON
@app.route('/api/faturas', methods=['POST'])
def criar_fatura():
    dados = request.get_json()
    paciente = dados.get('paciente')
    valor_servico = dados.get('valor_servico')

    if not paciente or valor_servico is None:
        return jsonify({'error': 'Campos obrigatórios: paciente, valor_servico'}), 400

    try:
        valor = float(valor_servico)
        if valor < 0:
            raise ValueError
    except:
        return jsonify({'error': 'valor_servico deve ser número positivo'}), 400

    imposto = valor * 0.10
    valor_total = valor + imposto

    fatura = {
        'id': len(faturas) + 1,
        'paciente': paciente,
        'valor_servico': valor,
        'imposto': round(imposto, 2),
        'valor_total': round(valor_total, 2)
    }
    faturas.append(fatura)
    return jsonify(fatura), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
