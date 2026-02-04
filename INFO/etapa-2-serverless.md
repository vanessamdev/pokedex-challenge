# Etapa 2 - Configuração Serverless

## O que foi feito

Configuração do Serverless Framework 3 para deploy da API Pokédex na AWS Lambda.

### Arquivos criados

- `serverless.yml` - Configuração do Serverless Framework
- `deploy.ps1` - Script PowerShell para empacotar dependências
- `requirements.txt` - Dependências do projeto (atualizado)

---

## Estrutura do serverless.yml

```yaml
service: pokedex-api
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.12
  stage: dev
  region: us-east-1
  memorySize: 256
  timeout: 30

functions:
  api:
    handler: app.main.handler
    events:
      - httpApi: ANY /{proxy+}
      - httpApi: ANY /
```

---

## Como fazer Deploy

### Opção 1: Serverless Framework (recomendado)

#### Pré-requisitos
1. Node.js instalado
2. AWS CLI configurado com credenciais

#### Passos

```bash
# Instalar Serverless Framework globalmente
npm install -g serverless

# Instalar plugin de dependências Python
npm install --save-dev serverless-python-requirements

# Configurar credenciais AWS (se ainda não configurou)
serverless config credentials --provider aws --key <AWS_KEY> --secret <AWS_SECRET>

# Deploy para dev
serverless deploy

# Deploy para produção
serverless deploy --stage prod
```

### Opção 2: Deploy Manual (sem Node.js)

```powershell
# Executar script de empacotamento
.\deploy.ps1

# O script gera: pokedex-api.zip
```

Depois, no AWS Console:
1. Acesse AWS Lambda
2. Crie uma nova função
3. Faça upload do `pokedex-api.zip`
4. Configure o handler: `app.main.handler`
5. Crie um API Gateway HTTP API
6. Conecte ao Lambda

---

## Comandos Úteis do Serverless

```bash
# Ver logs da função
serverless logs -f api

# Invocar função localmente
serverless invoke local -f api

# Remover stack da AWS
serverless remove

# Ver informações do deploy
serverless info
```

---

## Variáveis de Ambiente

| Variável | Descrição |
|----------|-----------|
| STAGE | Ambiente atual (dev, prod) |

---

## Endpoints após Deploy

Após o deploy, o Serverless mostrará a URL base. Os endpoints serão:

| Método | Endpoint |
|--------|----------|
| GET | `https://<api-id>.execute-api.<region>.amazonaws.com/treinadores` |
| POST | `https://<api-id>.execute-api.<region>.amazonaws.com/treinadores` |
| GET | `https://<api-id>.execute-api.<region>.amazonaws.com/pokemons` |
| POST | `https://<api-id>.execute-api.<region>.amazonaws.com/pokemons` |
| POST | `https://<api-id>.execute-api.<region>.amazonaws.com/batalhas` |

---

## Observações

- O banco de dados em memória será resetado a cada cold start do Lambda
- Para persistência real, implemente DynamoDB (próxima etapa)
- O Mangum faz a adaptação entre API Gateway e FastAPI automaticamente
