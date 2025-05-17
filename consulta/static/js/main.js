document.getElementById('consultaForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const nome_paciente = document.getElementById('nome_paciente').value.trim();
    const data = document.getElementById('data').value;
    const hora = document.getElementById('hora').value;

    if (!nome_paciente || !data || !hora) {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    const consulta = { nome_paciente, data, hora };

    try {
        const response = await fetch('/api/consultas', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(consulta)
        });

        const result = await response.json();

        if (!response.ok) {
            alert('Erro: ' + (result.error || 'Não foi possível agendar.'));
            return;
        }

        document.getElementById('consultaForm').reset();
        carregarConsultas();
    } catch (err) {
        alert('Erro ao conectar ao servidor.');
    }
});

async function carregarConsultas() {
    try {
        const response = await fetch('/api/consultas');
        const consultas = await response.json();

        const lista = document.getElementById('listaConsultas');
        lista.innerHTML = '';

        consultas.forEach(c => {
            const item = document.createElement('li');
            item.textContent = `Paciente: ${c.nome_paciente} | Data: ${c.data} | Hora: ${c.hora}`;
            lista.appendChild(item);
        });
    } catch (err) {
        console.error('Erro ao carregar consultas:', err);
    }
}

window.onload = carregarConsultas;
