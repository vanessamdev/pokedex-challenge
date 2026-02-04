# Iniciando o Projeto - API Pokédex

## Contexto do Desafio

Somos uma empresa que está desenvolvendo uma plataforma simples de gerenciamento de Pokémon, inspirada no conceito de uma Pokédex, com o objetivo de organizar treinadores e seus Pokémon de forma prática e padronizada.

A API REST permite:
- Cadastro e consulta de Treinadores
- Cadastro e consulta de Pokémon
- Relacionamento entre Treinadores e seus Pokémon
- Simulação de batalhas entre Pokémon

---

## Pré-requisitos

- Python 3.12+
- Node.js 18+ (para Serverless Framework)
- AWS CLI configurado (para deploy)
- Docker (opcional, para DynamoDB local)

---

## Etapa 1: Clonar/Copiar o Projeto

```bash
# Copie a pasta do projeto para a nova máquina
# Estrutura esperada:
```

```
pokedex-challenge/
├── app/
│   ├── __init__.py      # Inicializador do pacote Python
│   ├── main.py          # Endpoints FastAPI + handler Lambda
│   ├── models.py        # Modelos Pydantic para validação
│   ├── handlers.py      # Lógica de negócio (CRUD + batalhas)
│   ├── database.py      # Banco em memória (desenvolvimento)
│   └── dynamodb.py      # Módulo DynamoDB (produção)
├── doc/                 # Documentação do projeto
├── serverless.yml       # Configuração Serverless Framework
├── requirements.txt     # Dependências Python
└── deploy.ps1           # Script de empacotamento (Windows)
```

---

## Etapa 2: Criar Ambiente Virtual Python

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows PowerShell)
.\venv\Scripts\Activate

# Ativar ambiente virtual (Linux/Mac)
source venv/bin/activate
```

**Resultado esperado:**
```
# O prompt do terminal deve mostrar (venv) no início
(venv) PS C:\caminho\pokedex-challenge>
```

---

## Etapa 3: Instalar Dependências Python

```bash
# Instalar todas as dependências do projeto
pip install -r requirements.txt
```

**Conteúdo do requirements.txt:**
```python
fastapi      # Framework web para APIs REST
uvicorn      # Servidor ASGI para rodar localmente
mangum       # Adaptador FastAPI -> AWS Lambda
pydantic     # Validação de dados e serialização
boto3        # SDK AWS para DynamoDB
```

**Resultado esperado:**
```
Successfully installed fastapi uvicorn mangum pydantic boto3 ...
```

---

## Etapa 4: Testar API Localmente (Banco em Memória)

```bash
# Iniciar servidor de desenvolvimento
uvicorn app.main:app --reload --port 8000
```

**Resultado esperado:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process
INFO:     Application startup complete.
```

**Testar endpoints (novo terminal):**

```powershell
# Criar um treinador
Invoke-RestMethod -Uri "http://localhost:8000/treinadores" -Method POST -ContentType "application/json" -Body '{"nome": "Ash"}'

# Resultado esperado:
# id nome
# -- ----
#  1 Ash
```

```powershell
# Criar um pokémon
Invoke-RestMethod -Uri "http://localhost:8000/pokemons" -Method POST -ContentType "application/json" -Body '{"nome": "Pikachu", "tipo": "Eletrico", "nivel": 10, "treinador_id": 1}'

# Resultado esperado:
# id           : 1
# nome         : Pikachu
# tipo         : Eletrico
# nivel        : 10
# treinador_id : 1
```

**Acessar documentação interativa:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Etapa 5: Instalar Node.js e Serverless Framework

```bash
# Verificar se Node.js está instalado
node --version
# Resultado esperado: v18.x.x ou superior

npm --version
# Resultado esperado: 9.x.x ou superior
```

```bash
# Instalar Serverless Framework globalmente
npm install -g serverless

# Verificar instalação
serverless --version
# Resultado esperado: Framework Core: 3.x.x
```

---

## Etapa 6: Instalar Plugin de Dependências Python

```bash
# Inicializar package.json (na pasta do projeto)
npm init -y

# Instalar plugin para empacotar dependências Python
npm install --save-dev serverless-python-requirements
```

**Atualizar serverless.yml (adicionar plugin):**
```yaml
# serverless.yml - adicionar seção plugins

plugins:
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: false    # true se tiver Docker
    slim: true             # Remove arquivos desnecessários
    strip: false           # Mantém símbolos de debug
```

**Resultado esperado:**
```
added 1 package
```

---

## Etapa 7: Configurar Credenciais AWS

```bash
# Configurar credenciais AWS (substitua pelos seus valores)
serverless config credentials --provider aws --key SUA_ACCESS_KEY --secret SUA_SECRET_KEY

# Ou usar AWS CLI
aws configure
# AWS Access Key ID: SUA_ACCESS_KEY
# AWS Secret Access Key: SUA_SECRET_KEY
# Default region name: us-east-1
# Default output format: json
```

**Verificar configuração:**
```bash
aws sts get-caller-identity

# Resultado esperado:
# {
#     "UserId": "AIDAXXXXXXXXXX",
#     "Account": "123456789012",
#     "Arn": "arn:aws:iam::123456789012:user/seu-usuario"
# }
```

---

## Etapa 8: Testar Serverless Localmente (Offline)

```bash
# Instalar plugin serverless-offline
npm install --save-dev serverless-offline
```

**Adicionar ao serverless.yml:**
```yaml
plugins:
  - serverless-python-requirements
  - serverless-offline      # Adicionar esta linha
```

```bash
# Rodar API localmente simulando Lambda
serverless offline

# Resultado esperado:
# Starting Offline at stage dev (us-east-1)
# Offline listening on http://localhost:3000
```

**Testar endpoint local:**
```powershell
Invoke-RestMethod -Uri "http://localhost:3000/treinadores" -Method GET

# Resultado esperado: lista de treinadores (vazia inicialmente)
```

---

## Etapa 9: Deploy para AWS

```bash
# Deploy para ambiente de desenvolvimento
serverless deploy

# Resultado esperado:
# Deploying pokedex-api to stage dev (us-east-1)
# Service deployed to stack pokedex-api-dev
# endpoint: ANY - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com
# functions:
#   api: pokedex-api-dev-api
```

```bash
# Deploy para produção
serverless deploy --stage prod
```

**Testar endpoint na AWS:**
```powershell
# Substitua pela URL retornada no deploy
Invoke-RestMethod -Uri "https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/treinadores" -Method POST -ContentType "application/json" -Body '{"nome": "Ash"}'
```

---

## Etapa 10: Comandos Úteis do Serverless

```bash
# Ver informações do deploy
serverless info

# Resultado esperado:
# service: pokedex-api
# stage: dev
# region: us-east-1
# endpoint: https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com
```

```bash
# Ver logs da função Lambda
serverless logs -f api

# Ver logs em tempo real
serverless logs -f api --tail
```

```bash
# Remover stack da AWS (cuidado!)
serverless remove

# Resultado esperado:
# Removing pokedex-api from stage dev (us-east-1)
# Service pokedex-api has been successfully removed
```

---

## Etapa 11: Testar com DynamoDB Local (Opcional)

```bash
# Iniciar DynamoDB Local via Docker
docker run -p 8000:8000 amazon/dynamodb-local
```

```powershell
# Configurar variáveis de ambiente (PowerShell)
$env:USE_DYNAMODB="true"
$env:DYNAMODB_ENDPOINT="http://localhost:8000"

# Rodar API apontando para DynamoDB local
uvicorn app.main:app --reload --port 8001
```

---

## Resumo dos Comandos

| Etapa | Comando |
|-------|---------|
| Ativar venv | `.\venv\Scripts\Activate` |
| Instalar deps Python | `pip install -r requirements.txt` |
| Rodar local | `uvicorn app.main:app --reload` |
| Instalar Serverless | `npm install -g serverless` |
| Instalar plugins | `npm install --save-dev serverless-python-requirements serverless-offline` |
| Config AWS | `serverless config credentials --provider aws --key KEY --secret SECRET` |
| Rodar offline | `serverless offline` |
| Deploy dev | `serverless deploy` |
| Deploy prod | `serverless deploy --stage prod` |
| Ver logs | `serverless logs -f api --tail` |
| Remover | `serverless remove` |

---

## Estrutura do serverless.yml Completo

```yaml
service: pokedex-api

frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.12
  stage: ${opt:stage, 'dev'}
  region: ${opt:region, 'us-east-1'}
  memorySize: 256
  timeout: 30
  environment:
    STAGE: ${self:provider.stage}
    USE_DYNAMODB: "true"
  iam:
    role:
      statements:
        - Effect: Allow
          Action:
            - dynamodb:PutItem
            - dynamodb:GetItem
            - dynamodb:UpdateItem
            - dynamodb:DeleteItem
            - dynamodb:Scan
            - dynamodb:Query
          Resource:
            - !GetAtt TrainersTable.Arn
            - !GetAtt PokemonsTable.Arn
            - !GetAtt CountersTable.Arn

functions:
  api:
    handler: app.main.handler
    events:
      - httpApi:
          path: /{proxy+}
          method: ANY
      - httpApi:
          path: /
          method: ANY

plugins:
  - serverless-python-requirements
  - serverless-offline

custom:
  pythonRequirements:
    dockerizePip: false
    slim: true
    strip: false

resources:
  Resources:
    # Tabela de Treinadores
    TrainersTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: pokedex-trainers-${self:provider.stage}
        BillingMode: PAY_PER_REQUEST
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: N
        KeySchema:
          - AttributeName: id
            KeyType: HASH

    # Tabela de Pokémon
    PokemonsTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: pokedex-pokemons-${self:provider.stage}
        BillingMode: PAY_PER_REQUEST
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: N
        KeySchema:
          - AttributeName: id
            KeyType: HASH

    # Tabela de Contadores (para IDs)
    CountersTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: pokedex-counters-${self:provider.stage}
        BillingMode: PAY_PER_REQUEST
        AttributeDefinitions:
          - AttributeName: entity
            AttributeType: S
        KeySchema:
          - AttributeName: entity
            KeyType: HASH

package:
  patterns:
    - '!node_modules/**'
    - '!venv/**'
    - '!.git/**'
    - '!doc/**'
    - '!__pycache__/**'
    - '!*.md'
    - '!*.docx'
    - 'app/**'
    - 'requirements.txt'
```

---

## Troubleshooting

### Erro: "No module named 'app'"
```bash
# Certifique-se de estar na pasta raiz do projeto
cd pokedex-challenge
```

### Erro: "serverless: command not found"
```bash
# Reinstalar Serverless globalmente
npm install -g serverless
```

### Erro: "Access Denied" no deploy
```bash
# Verificar credenciais AWS
aws sts get-caller-identity

# Reconfigurar se necessário
serverless config credentials --provider aws --key KEY --secret SECRET --overwrite
```

### Erro: "Python requirements not found"
```bash
# Instalar plugin
npm install --save-dev serverless-python-requirements

# Limpar cache e tentar novamente
serverless requirements clean
serverless deploy
```


---

## Etapa 12: Executar Frontend Next.js

### Instalar dependências do frontend

```bash
cd frontend
npm install
```

**Resultado esperado:**
```
added 25 packages in 10s
```

### Executar frontend em desenvolvimento

```bash
# Terminal 1 - Backend (na pasta raiz)
uvicorn app.main:app --reload --port 8000

# Terminal 2 - Frontend (na pasta frontend)
cd frontend
npm run dev
```

**Resultado esperado:**
```
▲ Next.js 14.2.0
- Local:        http://localhost:3000
- Environments: .env.local

✓ Ready in 2s
```

### Acessar aplicação

- **Frontend:** http://localhost:3000
- **API Docs:** http://localhost:8000/docs

### Funcionalidades do Frontend

| Aba | Funcionalidades |
|-----|-----------------|
| Treinadores | Criar, Consultar (por ID ou todos), Deletar |
| Pokémons | Criar, Consultar (por ID ou todos), Deletar |
| Batalhas | Simular batalha entre dois pokémon |

### Build para produção

```bash
cd frontend
npm run build
npm start
```

---

## Resumo Completo dos Comandos

| Ação | Comando |
|------|---------|
| Ativar venv Python | `.\venv\Scripts\Activate` |
| Instalar deps Python | `pip install -r requirements.txt` |
| Rodar backend | `uvicorn app.main:app --reload` |
| Instalar deps frontend | `cd frontend && npm install` |
| Rodar frontend | `cd frontend && npm run dev` |
| Build frontend | `cd frontend && npm run build` |
| Instalar Serverless | `npm install -g serverless` |
| Deploy AWS | `serverless deploy` |
