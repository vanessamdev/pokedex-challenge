# Apresentação - API Pokédex

## Contexto

Somos uma empresa que está desenvolvendo uma plataforma simples de gerenciamento de Pokémon, inspirada no conceito de uma Pokédex, com o objetivo de organizar treinadores e seus Pokémon de forma prática e padronizada.

Precisamos de uma API REST que permita o cadastro e a consulta dessas informações, de forma simples, clara e bem estruturada, pois essa API servirá como base para futuras evoluções do sistema.

---

## Tecnologias Utilizadas

### Backend
| Tecnologia | Descrição |
|------------|-----------|
| Python 3.12+ | Linguagem principal |
| FastAPI | Framework web para APIs REST |
| Uvicorn | Servidor ASGI de alta performance |
| Pydantic | Validação de dados e serialização |
| Mangum | Adaptador FastAPI → AWS Lambda |
| Boto3 | SDK AWS para DynamoDB |

### Frontend
| Tecnologia | Descrição |
|------------|-----------|
| Next.js 14 | Framework React |
| TypeScript | Tipagem estática |
| React 18 | Biblioteca de UI |

### Infraestrutura
| Tecnologia | Descrição |
|------------|-----------|
| Serverless Framework 3 | Deploy e infraestrutura como código |
| AWS Lambda | Serverless compute |
| Amazon DynamoDB | Banco de dados NoSQL |
| API Gateway | Gerenciamento de APIs |

### Ferramentas
- Kiro IDE (desenvolvimento assistido por IA)
- python-docx (extração do documento .docx)

---

## Estrutura do Projeto

```
pokedex-challenge/
├── app/                         # Backend Python
│   ├── __init__.py              # Inicializador do pacote
│   ├── main.py                  # Endpoints FastAPI + handler Lambda
│   ├── models.py                # Modelos Pydantic (validação)
│   ├── handlers.py              # Lógica de negócio (CRUD + batalhas)
│   ├── database.py              # Banco em memória (desenvolvimento)
│   └── dynamodb.py              # Módulo DynamoDB (produção)
├── frontend/                    # Frontend Next.js
│   ├── package.json             # Dependências Node.js
│   ├── tsconfig.json            # Configuração TypeScript
│   ├── next.config.js           # Configuração Next.js (proxy API)
│   └── src/
│       ├── app/
│       │   ├── globals.css      # Tema dark verde água
│       │   ├── layout.tsx       # Layout principal
│       │   └── page.tsx         # Página principal (abas)
│       └── lib/
│           └── api.ts           # Funções de acesso à API
├── doc/                         # Documentação
│   ├── challenge.md             # Documento do desafio em Markdown
│   ├── etapa-1.md               # Implementação inicial da API
│   ├── etapa-2-serverless.md    # Configuração Serverless
│   ├── etapa-3-dynamodb.md      # Integração DynamoDB
│   ├── etapa-4-frontend.md      # Frontend Next.js
│   ├── iniciando-projeto.md     # Guia passo a passo
│   └── apresentacao.md          # Este arquivo
├── challenge.py                 # Documento do desafio em Python
├── serverless.yml               # Configuração Serverless Framework
├── requirements.txt             # Dependências Python
├── start.ps1                    # Script iniciar projeto (Windows)
├── start.sh                     # Script iniciar projeto (Linux/Mac)
├── test-api.ps1                 # Script de testes (Windows)
├── test-api.sh                  # Script de testes (Linux/Mac)
└── deploy.ps1                   # Script de empacotamento para deploy
```

---

## Como Iniciar o Projeto

### Opção 1: Script Automático

**Windows (PowerShell):**
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
# Criar e ativar ambiente virtual
python -m venv venv
.\venv\Scripts\Activate    # Windows
source venv/bin/activate   # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Iniciar backend
uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### Acessar
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs (Swagger):** http://localhost:8000/docs
- **API Docs (ReDoc):** http://localhost:8000/redoc

---

## Endpoints da API

### Treinadores

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/treinadores` | Lista todos os treinadores |
| GET | `/treinadores/{id}` | Busca treinador por ID |
| POST | `/treinadores` | Cria um treinador |
| PUT | `/treinadores/{id}` | Atualiza um treinador |
| DELETE | `/treinadores/{id}` | Deleta treinador e seus pokémon |

### Pokémon

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/pokemons` | Lista todos os pokémon |
| GET | `/pokemons/{id}` | Busca pokémon por ID |
| POST | `/pokemons` | Cria um pokémon |
| PUT | `/pokemons/{id}` | Atualiza um pokémon |
| DELETE | `/pokemons/{id}` | Deleta um pokémon |

### Relacionamento

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/treinadores/{id}/pokemons` | Lista pokémon de um treinador |

### Batalhas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/batalhas` | Simula batalha entre dois pokémon |

---

## Testes da API

### Script Automático

**Windows:**
```powershell
.\test-api.ps1

# Testar em porta diferente
.\test-api.ps1 -BaseUrl "http://localhost:3000"
```

**Linux/Mac:**
```bash
chmod +x test-api.sh
./test-api.sh

# Testar em porta diferente
./test-api.sh http://localhost:3000
```

### Testes Manuais (PowerShell)

```powershell
# Criar treinador
Invoke-RestMethod -Uri "http://localhost:8000/treinadores" -Method POST -ContentType "application/json" -Body '{"nome": "Ash"}'

# Criar pokémon
Invoke-RestMethod -Uri "http://localhost:8000/pokemons" -Method POST -ContentType "application/json" -Body '{"nome": "Pikachu", "tipo": "Eletrico", "nivel": 10, "treinador_id": 1}'

# Listar treinadores
Invoke-RestMethod -Uri "http://localhost:8000/treinadores" -Method GET

# Listar pokémon
Invoke-RestMethod -Uri "http://localhost:8000/pokemons" -Method GET

# Batalha
Invoke-RestMethod -Uri "http://localhost:8000/batalhas" -Method POST -ContentType "application/json" -Body '{"pokemon_atacante_id": 1, "pokemon_defensor_id": 2}'

# Deletar pokémon
Invoke-RestMethod -Uri "http://localhost:8000/pokemons/1" -Method DELETE

# Deletar treinador (e seus pokémon)
Invoke-RestMethod -Uri "http://localhost:8000/treinadores/1" -Method DELETE
```

### Testes via Insomnia/Postman

| Método | URL | Body |
|--------|-----|------|
| POST | `/treinadores` | `{"nome": "Ash"}` |
| GET | `/treinadores` | - |
| GET | `/treinadores/1` | - |
| PUT | `/treinadores/1` | `{"nome": "Ash Ketchum"}` |
| DELETE | `/treinadores/1` | - |
| POST | `/pokemons` | `{"nome": "Pikachu", "tipo": "Eletrico", "nivel": 10, "treinador_id": 1}` |
| GET | `/pokemons` | - |
| GET | `/pokemons/1` | - |
| DELETE | `/pokemons/1` | - |
| GET | `/treinadores/1/pokemons` | - |
| POST | `/batalhas` | `{"pokemon_atacante_id": 1, "pokemon_defensor_id": 2}` |

---

## Regras de Negócio

### Validações
- Treinador: nome obrigatório
- Pokémon: nome, tipo e treinador_id obrigatórios
- Pokémon: nível mínimo = 1
- Pokémon: treinador_id deve existir
- Batalha: pokémon não pode batalhar contra si mesmo
- Batalha: ambos pokémon devem existir
- DELETE treinador: remove também todos os pokémon do treinador

### Regras de Batalha
1. Pokémon com nível mais alto vence
2. Em caso de empate de nível, o tipo decide:
   - Fogo vence Planta
   - Planta vence Água
   - Água vence Fogo
3. Se nível e tipo forem equivalentes, resultado é empate

### Normalização de Tipos
A API normaliza os tipos para comparação (case-insensitive, sem acentos):
- "Fogo", "fogo", "FOGO" → fogo
- "Água", "agua", "AGUA" → agua
- "Planta", "planta" → planta

---

## Frontend (Next.js)

### Características
- **Framework:** Next.js 14 com TypeScript
- **Tema:** Dark mode com tons em verde água (#2dd4bf)
- **Layout:** Centralizado e responsivo

### Funcionalidades
- Abas de navegação: Treinadores, Pokémons, Batalhas
- CRUD completo para Treinadores e Pokémon
- Simulação de batalhas com resultado visual
- Mensagens de feedback (sucesso/erro)

### Layout
```
┌─────────────────────────────────────┐
│         🎮 Pokédex API              │
├─────────────────────────────────────┤
│  [Treinadores] [Pokémons] [Batalhas]│
├─────────────────────────────────────┤
│  ┌─────────────────────────────┐    │
│  │  Campo de entrada           │    │
│  │  Campo de entrada           │    │
│  │  [Criar] [Consultar] [Deletar]   │
│  └─────────────────────────────┘    │
├─────────────────────────────────────┤
│  ┌─────────────────────────────┐    │
│  │  Resultado / Card           │    │
│  └─────────────────────────────┘    │
│  ┌─────────────────────────────┐    │
│  │  Resultado / Card           │    │
│  └─────────────────────────────┘    │
└─────────────────────────────────────┘
```

### Cores do Tema
| Elemento | Cor |
|----------|-----|
| Background | #0d1117 |
| Cards | #161b22 |
| Accent (verde água) | #2dd4bf |
| Accent hover | #14b8a6 |
| Texto | #f0f6fc |
| Texto secundário | #8b949e |
| Erro | #f85149 |
| Sucesso | #3fb950 |

---

## Deploy Serverless (AWS)

### Configurar Credenciais AWS

```bash
serverless config credentials --provider aws --key <KEY> --secret <SECRET>
```

### Deploy

```bash
# Instalar Serverless (requer Node.js)
npm install -g serverless

# Deploy para desenvolvimento
serverless deploy

# Deploy para produção
serverless deploy --stage prod
```

### Comandos Úteis

```bash
serverless info          # Info do deploy
serverless logs -f api   # Ver logs
serverless remove        # Remover stack
```

---

## Banco de Dados DynamoDB

### Tabelas (criadas automaticamente no deploy)

| Tabela | Chave | Descrição |
|--------|-------|-----------|
| pokedex-trainers-{stage} | id (Number) | Treinadores |
| pokedex-pokemons-{stage} | id (Number) | Pokémon |
| pokedex-counters-{stage} | entity (String) | Contadores para IDs |

### Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| USE_DYNAMODB | Ativa DynamoDB | "false" |
| DYNAMODB_ENDPOINT | URL do DynamoDB local | None |
| AWS_REGION | Região AWS | "us-east-1" |
| STAGE | Ambiente (dev/prod) | "dev" |

### Executar com DynamoDB Local

```bash
# Iniciar DynamoDB Local (Docker)
docker run -p 8000:8000 amazon/dynamodb-local

# Configurar variáveis (PowerShell)
$env:USE_DYNAMODB="true"
$env:DYNAMODB_ENDPOINT="http://localhost:8000"

# Iniciar API
uvicorn app.main:app --reload --port 8001
```

---

## Scripts Disponíveis

| Script | Sistema | Descrição |
|--------|---------|-----------|
| `start.ps1` | Windows | Inicia backend + frontend automaticamente |
| `start.sh` | Linux/Mac | Inicia backend + frontend automaticamente |
| `test-api.ps1` | Windows | Executa testes em todos os endpoints |
| `test-api.sh` | Linux/Mac | Executa testes em todos os endpoints |
| `deploy.ps1` | Windows | Empacota projeto para deploy manual |

---

## Etapas de Desenvolvimento

| Etapa | Descrição | Status |
|-------|-----------|--------|
| 1 | Implementação inicial da API (CRUD + Batalhas) | ✅ Concluído |
| 2 | Configuração Serverless Framework 3 | ✅ Concluído |
| 3 | Integração com DynamoDB | ✅ Concluído |
| 4 | Implementação DELETE endpoints | ✅ Concluído |
| 5 | Frontend Next.js (tema dark verde água) | ✅ Concluído |
| 6 | Scripts de automação (start/test) | ✅ Concluído |

---

## Testes Realizados

| Teste | Resultado |
|-------|-----------|
| Criar treinadores | ✅ Passou |
| Listar treinadores | ✅ Passou |
| Buscar treinador por ID | ✅ Passou |
| Atualizar treinador | ✅ Passou |
| Deletar treinador | ✅ Passou |
| Criar pokémon | ✅ Passou |
| Listar pokémon | ✅ Passou |
| Buscar pokémon por ID | ✅ Passou |
| Atualizar pokémon | ✅ Passou |
| Deletar pokémon | ✅ Passou |
| Listar pokémon de um treinador | ✅ Passou |
| Batalha por nível (maior vence) | ✅ Passou |
| Batalha por tipo (Fogo > Planta) | ✅ Passou |
| Batalha por tipo (Água > Fogo) | ✅ Passou |
| Batalha por tipo (Planta > Água) | ✅ Passou |
| Empate (mesmo nível, tipo neutro) | ✅ Passou |
| Validação: batalha contra si mesmo | ✅ Passou |
| Validação: pokémon sem treinador | ✅ Passou |

---

## Observações

- Por padrão, a API usa banco em memória (dados perdidos ao reiniciar)
- Com `USE_DYNAMODB=true`, os dados são persistidos no DynamoDB
- O deploy via Serverless Framework cria automaticamente as tabelas DynamoDB
- A documentação interativa (Swagger) é gerada automaticamente pelo FastAPI
- O frontend usa proxy para evitar problemas de CORS em desenvolvimento
