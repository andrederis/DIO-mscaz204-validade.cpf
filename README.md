# Deploy de uma API na Nuvem (Simulação) — Azure Functions + Python

Projeto para **deploy de uma API na nuvem (Azure).  
O foco é demonstrar a estrutura e funcionamento do serviço.

**Repositório GitHub:** [https://andrederis/DIO-mscaz204-validade.cpf] 
**Deploy :** [https://andrederiswebapp.azurewebsites.net/api/validate-cpf]

---

## O que a API faz
API criada com **Azure Functions (Python)** que valida **números de CPF** usando o cálculo de dígitos verificadores (módulo 11).

Exemplo de uso:
GET /api/validate-cpf?cpf=52998224725
→ {"ok": true, "cpf": "52998224725"}

Também é possível usar o `index.html` como interface simples para teste.

---

## Como rodar localmente
**Pré-requisitos:**
- Python 3.9+ (recomendado 3.11)
- Azure Functions Core Tools v4 (`func`)
- VS Code com extensão Azure Functions

### Passos:
```bash
# 1. Criar ambiente virtual
python -m venv .venv
# 2. Ativar ambiente
.\.venv\Scripts\Activate.ps1   # (Windows PowerShell)
# 3. Instalar dependências
pip install -r requirements.txt
# 4. Rodar o projeto localmente
func start


Acesse no navegador:
http://localhost:7071/api/validate-cpf?cpf=52998224725

Ou abra o index.html e teste pelo botão na página (usar Go Server ou similar).

Estrutura do projeto
function_app.py         # Lógica principal (Azure Function)
index.html              # Front-end HTML com JS para teste
requirements.txt        # Dependências (azure-functions)
host.json               # Configurações do runtime
local.settings.json     # Configurações locais (não vai para produção)

Simulação de Deploy na Azure

(não publicado neste repositório, apenas demonstrativo)

Passos que seriam seguidos:

Login no Azure via VS Code

Criar Function App (Plano Consumption, Python 3.11, Linux)

Deploy via comando:

Azure Functions: Deploy to Function App


URL
https://andrederiswebapp.azurewebsites.net/api/validate-cpf

Custo: Plano Consumption é gratuito dentro da cota (1 milhão de execuções/mês).

Tecnologias usadas:

Azure Functions (Python 3.11)

JavaScript (fetch API)

HTML + CSS (Front-end simples)

VS Code + Azure Core Tools