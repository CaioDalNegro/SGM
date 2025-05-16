# SGM

# 🏥 Sistema de Gestão Modular - Vida+ Saúde

Este projeto implementa um **Sistema de Gestão para Clínicas Médicas** utilizando uma arquitetura baseada em **microsserviços**, desenvolvido em **Python com Flask** e **containerizado com Docker**. Ele permite o gerenciamento descentralizado de pacientes, consultas, prontuários e faturamento médico.

---

## 📦 Visão Geral

Com o crescimento da rede Vida+ Saúde, houve a necessidade de abandonar o antigo sistema monolítico. A solução proposta adota uma arquitetura de microsserviços, onde cada componente do sistema é executado de forma isolada, promovendo:

- **Escalabilidade**
- **Manutenção simplificada**
- **Resiliência entre serviços**
- **Integração facilitada com sistemas externos**

---

## 🧩 Microsserviços

O sistema é composto pelos seguintes microsserviços:

|          Serviço         |                 Descrição                    | Porta  |
|--------------------------|----------------------------------------------|--------|
|       **Paciente**       |       Cadastro e busca de pacientes          | 5001   |
|       **Consulta**       |     Agendamento e listagem de consultas      | 5002   |
|      **Prontuário**      |  Armazenamento e acesso a registros médicos  | 5003   |
|     **Faturamento**      |   Geração de faturas e cálculo de valores    | 5004   |

---

## 🔧 Tecnologias Utilizadas

- **Python 3.10**
- **Flask**
- **Docker / Docker Compose**
- **HTTP (RESTful APIs)**
- **Requests (para comunicação entre serviços)**

---

## 🔗 Arquitetura

- **Integração Horizontal**: Serviços se comunicam via chamadas HTTP internas (ex: Consulta consulta o serviço de Paciente).
- **Integração Vertical**: O serviço de Faturamento se comunica com o serviço externo simulado de Plano de Saúde.

### 📌 Diagrama de Arquitetura

> 💡 *Insira aqui uma imagem do diagrama, ou utilize um serviço como draw.io para gerar um esquema visual.*  
> Exemplo (substitua pelo seu):
> ![Diagrama de Arquitetura](docs/diagrama-arquitetura.png)

---

## 🚀 Como Executar

> Requisitos: [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/vida-saude.git
cd vida-saude

# Suba todos os serviços
docker-compose up --build

