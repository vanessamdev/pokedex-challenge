# Etapa 3 - Integração com DynamoDB

## O que foi feito

Implementação do Amazon DynamoDB como banco de dados persistente para a API Pokédex.

### Arquivos criados/modificados

- `app/dynamodb.py` - Módulo de acesso ao DynamoDB
- `app/handlers.py` - Atualizado para suportar DynamoDB ou banco em memória
- `serverless.yml` - Atualizado com criação das tabelas e permissões IAM
- `requirements.txt` - Adicionado boto3

---

## Tabelas DynamoDB

| Tabela | Chave | Descrição |
|--------|-------|-----------|
| pokedex-trainers-{stage} | id (Number) | Armazena treinadores |
| pokedex-pokemons-{stage} | id (Number) | Armazena pokémon |
| pokedex-counters-{stage} | entity (String) | Contadores para IDs |

---

## Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| USE_DYNAMODB | Ativa DynamoDB | "false" |
| DYNAMODB_ENDPOINT | URL do DynamoDB local | None |
| AWS_REGION | Região AWS | "us-east-1" |
| STAGE | Ambiente | "dev" |

---

## Execução Local

### Opção 1: Banco em memória (padrão)

```bash
uvicorn app.main:app --reload
```

### Opção 2: DynamoDB Local

```bash
# Instalar e iniciar DynamoDB Local (Docker)
docker run -p 8000:8000 amazon/dynamodb-local

# Criar tabelas locais
python scripts/create_tables.py

# Executar com DynamoDB
$env:USE_DYNAMODB="true"
$env:DYNAMODB_ENDPOINT="http://localhost:8000"
uvicorn app.main:app --reload --port 8001
```

---

## Permissões IAM (AWS)

O serverless.yml configura automaticamente:
- dynamodb:PutItem
- dynamodb:GetItem
- dynamodb:UpdateItem
- dynamodb:DeleteItem
- dynamodb:Scan
- dynamodb:Query
