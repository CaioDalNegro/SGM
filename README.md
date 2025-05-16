# SGM

# 🏥 Sistema de Gestão Modular - Vida+ Saúde

Este projeto implementa um sistema de gestão para uma rede de clínicas médicas com arquitetura baseada em **microsserviços**, desenvolvido em **Python com Flask** e **containerizado com Docker**.

## 📦 Visão Geral

Com o crescimento da rede Vida+ Saúde, o antigo sistema monolítico deu lugar a uma arquitetura mais escalável e modular. Os serviços são organizados em contêineres independentes, facilitando a manutenção, escalabilidade e integração com sistemas externos.

---

## 🧩 Microsserviços

O sistema é composto pelos seguintes microsserviços:

|          Serviço         |                 Descrição                    | Porta  |
|--------------------------|----------------------------------------------|--------|
|       **Paciente**       |       Cadastro e busca de pacientes          | 5001   |
|       **Consulta**       |     Agendamento e listagem de consultas      | 5002   |
|      **Prontuário**      |  Armazenamento e acesso a registros médicos  | 5003   |
|     **Faturamento**      |   Geração de faturas e cálculo de valores    | 5004   |
| **Plano de Saúde** (mock)| Serviço simulado para validação de cobertura | 5005   |

---

## 🔗 Arquitetura

- **Integração Horizontal**: Comunicação entre microsserviços por chamadas HTTP internas (ex: Consulta busca dados do Paciente).
- **Integração Vertical**: Comunicação com um serviço externo simulado (Plano de Saúde) para validação de procedimentos.

### 📌 Diagrama Resumido

