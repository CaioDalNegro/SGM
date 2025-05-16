// Função para formatar CPF no padrão 000.000.000-00 enquanto o usuário digita
function formatarCPF(value) {
    // Remove tudo que não for número
    value = value.replace(/\D/g, "");
    // Limita a 11 dígitos
    value = value.substring(0, 11);

    // Aplica máscara
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

    return value;
}

// Função para formatar telefone no padrão (00) 0000-0000 ou (00) 00000-0000
function formatarTelefone(value) {
    // Remove tudo que não for número
    value = value.replace(/\D/g, "");
    // Limita a 11 dígitos
    value = value.substring(0, 11);

    if (value.length <= 10) {
        // Formato para telefone fixo: (00) 0000-0000
        value = value.replace(/(\d{2})(\d{4})(\d{0,4})/, "($1) $2-$3");
    } else {
        // Formato para celular: (00) 00000-0000
        value = value.replace(/(\d{2})(\d{5})(\d{0,4})/, "($1) $2-$3");
    }

    return value;
}

// Função para carregar e mostrar os pacientes na lista
function carregarPacientes() {
    fetch("/api/pacientes")
        .then(response => response.json())
        .then(data => {
            const lista = document.getElementById("listaPacientes");
            lista.innerHTML = ""; // Limpa a lista antes de preencher

            data.forEach(paciente => {
                // Formata CPF e telefone para exibição
                const cpfFormatado = formatarCPF(paciente.cpf);
                const telefoneFormatado = formatarTelefone(paciente.telefone);

                const li = document.createElement("li");
                li.textContent = `${paciente.nome} - CPF: ${cpfFormatado} - Telefone: ${telefoneFormatado}`;
                lista.appendChild(li);
            });
        })
        .catch(err => {
            console.error("Erro ao carregar pacientes:", err);
        });
}

// Chama carregarPacientes ao abrir a página
window.addEventListener("load", carregarPacientes);

// Evento para formatar CPF enquanto digita
document.getElementById("cpf").addEventListener("input", function (e) {
    e.target.value = formatarCPF(e.target.value);
});

// Evento para formatar telefone enquanto digita
document.getElementById("telefone").addEventListener("input", function (e) {
    e.target.value = formatarTelefone(e.target.value);
});

// Validação ao enviar o formulário
document.getElementById("pacienteForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const cpf = document.getElementById("cpf").value.replace(/\D/g, "");
    const telefone = document.getElementById("telefone").value.replace(/\D/g, "");

    if (cpf.length !== 11) {
        alert("CPF deve conter 11 números.");
        return;
    }

    if (telefone.length < 10 || telefone.length > 11) {
        alert("Telefone deve conter 10 ou 11 números.");
        return;
    }

    // Se a validação passar, envie os dados para o backend (exemplo com fetch)
    const nome = document.getElementById("nome").value;

    fetch("/api/pacientes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, cpf, telefone }),
    })
    .then(response => {
        if (response.ok) {
            alert("Paciente cadastrado com sucesso!");
            document.getElementById("pacienteForm").reset();
            // Recarregue a lista de pacientes ou atualize a UI conforme necessário
        } else {
            alert("Erro ao cadastrar paciente.");
        }
    })
    .catch(() => alert("Erro na comunicação com o servidor."));
});
