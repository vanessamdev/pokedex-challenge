# 🎮 Pokédex API

API REST para gerenciamento de Treinadores e Pokémon, com sistema de batalhas e frontend em Next.js.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Next.js](https://img.shields.io/badge/Next.js-14-black)
![AWS](https://img.shields.io/badge/AWS-Lambda%20%2B%20DynamoDB-orange)

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação](#-instalação)
- [Executar Localmente](#-executar-localmente)
- [Executar com Serverless Offline](#-executar-com-serverless-offline)
- [Deploy na AWS](#-deploy-na-aws)
- [Endpoints da API](#-endpoints-da-api)
- [Regras de Batalha](#-regras-de-batalha)
- [Scripts Disponíveis](#-scripts-disponíveis)
- [Frontend](#-frontend)

---

## 📖 Sobre o Projeto

Plataforma de gerenciamento de Pokémon inspirada no conceito de uma Pokédex, permitindo:

- ✅ CRUD completo de Treinadores
- ✅ CRUD completo de Pokémon
- ✅ Relacionamento Treinador ↔ Pokémon
- ✅ Sistema de batalhas com regras de tipo
- ✅ Frontend responsivo com tema dark
- ✅ Deploy serverless na AWS

---

## 🛠 Tecnologias

### Backend
| Tecnologia | Descrição |
|------------|-----------|
| Python 3.12+ | Linguagem principal |
| FastAPI | Framework web para APIs |
| Uvicorn | Servidor ASGI |
| Pydantic | Validação de dados |
| Boto3 | SDK AWS (DynamoDB) |
| Mangum | Adaptador para AWS Lambda |

### Frontend
| Tecnologia | Descrição |
|------------|-----------|
| Next.js 14 | Framework React |
| TypeScript | Tipagem estática |
| React 18 | Biblioteca de UI |

### Infraestrutura
| Tecnologia | Descrição |
|------------|-----------|
| Serverless Framework 3 | Deploy e IaC |
| AWS Lambda | Compute serverless |
| Amazon DynamoDB | Banco NoSQL |
| API Gateway | Gerenciamento de APIs |

---

## 📁 Estrutura do Projeto (Arquitetura SOLID)

```
pokedex-challenge/
├── app/                              # Backend Python (SOLID)
│   ├── __init__.py
│   ├── main.py                       # Endpoints REST (Controller)
│   ├── models.py                     # Modelos Pydantic (DTOs)
│   ├── dependencies.py               # Injeção de Dependências (D)
│   ├── interfaces/                   # Contratos Abstratos (D)
│   │   ├── __init__.py
│   │   └── database_interface.py     # Interfaces de repositório
│   ├── repositories/                 # Acesso a Dados (S)
│   │   ├── __init__.py
│   │   ├── memory_repository.py      # Implementação em memória
│   │   └── dynamodb_repository.py    # Implementação DynamoDB
│   └── services/                     # Lógica de Negócio (S)
│       ├── __init__.py
│       ├── trainer_service.py        # Serviço de Treinadores
│       ├── pokemon_service.py        # Serviço de Pokémon
│       └── battle_service.py         # Serviço de Batalhas
├── frontend/                         # Frontend Next.js
│   ├── package.json
│   ├── next.config.js
│   └── src/
│       ├── app/
│       │   ├── globals.css           # Tema dark verde água
│       │   ├── layout.tsx
│       │   └── page.tsx
│       └── lib/
│           └── api.ts                # Cliente API
├── INFO/                             # Documentação Acadêmica
│   ├── apresentacao.md               # Apresentação do projeto
│   ├── challenge.md                  # Desafio original
│   ├── challenge.py                  # Desafio em Python
│   ├── etapa-1.md                    # Etapa 1 - API
│   ├── etapa-2-serverless.md         # Etapa 2 - Serverless
│   ├── etapa-3-dynamodb.md           # Etapa 3 - DynamoDB
│   ├── etapa-4-frontend.md           # Etapa 4 - Frontend
│   └── iniciando-projeto.md          # Guia de instalação
├── serverless.yml                    # Config AWS Lambda
├── requirements.txt                  # Deps Python
├── README.md                         # Este arquivo
├── start.ps1 / start.sh              # Scripts de inicialização
└── test-api.ps1 / test-api.sh        # Scripts de teste
```

### Princípios SOLID Aplicados

| Princípio | Aplicação |
|-----------|-----------|
| **S** - Single Responsibility | Cada service/repository tem uma única responsabilidade |
| **O** - Open/Closed | Novos repositórios podem ser adicionados sem modificar services |
| **L** - Liskov Substitution | Memory e DynamoDB repositories são intercambiáveis |
| **I** - Interface Segregation | Interfaces separadas para Trainer e Pokemon |
| **D** - Dependency Inversion | Services dependem de interfaces, não implementações |

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.12+
- Node.js 18+
- Git

### Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/pokedex-challenge.git
cd pokedex-challenge
```

### Instalar Dependências do Backend

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows PowerShell)
.\venv\Scripts\Activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### Instalar Dependências do Frontend

```bash
cd frontend
npm install
cd ..
```

---

## 💻 Executar Localmente

### Opção 1: Script Automático

**Windows:**
```powershell
.\start.ps1
```

**Linux/Mac:**
```bash
chmod +x start.sh
./start.sh
```

### Opção 2: Manual

**Terminal 1 - Backend:**
```bash
uvicorn app.main:app --reload --port 3000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev -- -p 3001
```

### Acessar

| Serviço | URL |
|---------|-----|
| Frontend | http://localhost:3001 |
| Backend API | http://localhost:3000 |
| Swagger Docs | http://localhost:3000/docs |
| ReDoc | http://localhost:3000/redoc |

---

## ⚡ Executar com Serverless Offline

### Instalar Serverless Framework

```bash
npm install -g serverless
```

### Instalar Plugins

```bash
npm init -y
npm install --save-dev serverless-python-requirements serverless-offline
```

### Executar Offline

```bash
serverless offline
```

A API estará disponível em: http://localhost:3000

---

## ☁️ Deploy na AWS

### 1. Configurar Credenciais AWS

```bash
serverless config credentials --provider aws --key SUA_ACCESS_KEY --secret SUA_SECRET_KEY
```

Ou via AWS CLI:
```bash
aws configure
```

### 2. Deploy para Desenvolvimento

```bash
serverless deploy
```

### 3. Deploy para Produção

```bash
serverless deploy --stage prod
```

### 4. Verificar Deploy

```bash
serverless info
```

### 5. Ver Logs

```bash
serverless logs -f api --tail
```

### 6. Remover Stack

```bash
serverless remove
```

### Recursos Criados na AWS

- 1 Lambda Function
- 1 API Gateway HTTP API
- 3 Tabelas DynamoDB:
  - `pokedex-trainers-{stage}`
  - `pokedex-pokemons-{stage}`
  - `pokedex-counters-{stage}`

---

## 📡 Endpoints da API

### Treinadores

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/treinadores` | Lista todos |
| GET | `/treinadores/{id}` | Busca por ID |
| POST | `/treinadores` | Cria treinador |
| PUT | `/treinadores/{id}` | Atualiza |
| DELETE | `/treinadores/{id}` | Deleta (e seus pokémon) |

### Pokémon

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/pokemons` | Lista todos |
| GET | `/pokemons/{id}` | Busca por ID |
| POST | `/pokemons` | Cria pokémon |
| PUT | `/pokemons/{id}` | Atualiza |
| DELETE | `/pokemons/{id}` | Deleta |

### Relacionamento

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/treinadores/{id}/pokemons` | Pokémon do treinador |

### Batalhas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/batalhas` | Simula batalha |

### Exemplos de Requisição

```bash
# Criar treinador
curl -X POST http://localhost:3000/treinadores \
  -H "Content-Type: application/json" \
  -d '{"nome": "Ash"}'

# Criar pokémon
curl -X POST http://localhost:3000/pokemons \
  -H "Content-Type: application/json" \
  -d '{"nome": "Pikachu", "tipo": "Eletrico", "nivel": 10, "treinador_id": 1}'

# Batalha
curl -X POST http://localhost:3000/batalhas \
  -H "Content-Type: application/json" \
  -d '{"pokemon_atacante_id": 1, "pokemon_defensor_id": 2}'
```

---

## ⚔️ Regras de Batalha

1. **Nível maior vence**
2. **Em caso de empate de nível, o tipo decide:**
   - 🔥 Fogo vence 🌿 Planta
   - 🌿 Planta vence 💧 Água
   - 💧 Água vence 🔥 Fogo
3. **Se nível e tipo forem iguais: Empate**

### Validações
- Pokémon não pode batalhar contra si mesmo
- Ambos pokémon devem existir
- Pokémon deve ter treinador

---

## 📜 Scripts Disponíveis

| Script | Sistema | Comando | Descrição |
|--------|---------|---------|-----------|
| start.ps1 | Windows | `.\start.ps1` | Inicia backend + frontend |
| start.sh | Linux/Mac | `./start.sh` | Inicia backend + frontend |
| test-api.ps1 | Windows | `.\test-api.ps1` | Testa todos endpoints |
| test-api.sh | Linux/Mac | `./test-api.sh` | Testa todos endpoints |
| deploy.ps1 | Windows | `.\deploy.ps1` | Empacota para deploy |

### Testar em porta diferente

```powershell
.\test-api.ps1 -BaseUrl "http://localhost:3000"
```

```bash
./test-api.sh http://localhost:3000
```

---

## 🎨 Frontend

### Características

- **Framework:** Next.js 14 + TypeScript
- **Tema:** Dark mode com verde água (#2dd4bf)
- **Layout:** Centralizado e responsivo

### Funcionalidades

- Abas: Treinadores | Pokémons | Batalhas
- CRUD completo via interface
- Resultado de batalhas visual
- Mensagens de feedback

### Configuração da API

Edite `frontend/src/lib/api.ts`:

```typescript
const API_URL = 'http://localhost:3000'  // Ajuste conforme necessário
```

---

## 🔧 Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| USE_DYNAMODB | Usar DynamoDB | "false" |
| DYNAMODB_ENDPOINT | URL DynamoDB local | None |
| AWS_REGION | Região AWS | "us-east-1" |
| STAGE | Ambiente | "dev" |

### Usar DynamoDB Local

```bash
# Iniciar DynamoDB Local (Docker)
docker run -p 8000:8000 amazon/dynamodb-local

# Configurar variáveis
export USE_DYNAMODB=true
export DYNAMODB_ENDPOINT=http://localhost:8000

# Iniciar API
uvicorn app.main:app --reload --port 3000
```

---

## 📄 Licença

Este projeto foi desenvolvido como parte de um desafio técnico.

---

## 👤 Autor

Desenvolvido com auxílio do Kiro IDE.
