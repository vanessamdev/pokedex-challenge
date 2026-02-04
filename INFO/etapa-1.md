# Etapa 1 - Implementação da API Pokédex

## O que foi feito

Analisei o documento "Desafio - Desenvolvimento (2).docx" e implementei uma API REST completa de Pokédex usando FastAPI.

### Arquivos criados

- `app/models.py` - Modelos Pydantic para validação de dados (Treinadores, Pokémon, Batalhas)
- `app/database.py` - Banco de dados em memória (simulação simples)
- `app/handlers.py` - Lógica de negócio e regras de batalha
- `app/main.py` - Rotas da API e handler para AWS Lambda (Mangum)
- `app/__init__.py` - Inicializador do pacote
- `requirements.txt` - Dependências do projeto

### Endpoints implementados

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /treinadores | Lista todos os treinadores |
| GET | /treinadores/{id} | Busca um treinador |
| POST | /treinadores | Cadastra um treinador |
| PUT | /treinadores/{id} | Atualiza um treinador |
| GET | /pokemons | Lista todos os Pokémon |
| GET | /pokemons/{id} | Busca um Pokémon |
| POST | /pokemons | Cadastra um Pokémon |
| PUT | /pokemons/{id} | Atualiza um Pokémon |
| GET | /treinadores/{id}/pokemons | Lista Pokémon de um treinador |
| POST | /batalhas | Simula batalha entre dois Pokémon |

### Regras de negócio implementadas

- Treinador pode ter vários Pokémon
- Pokémon pertence a apenas um treinador
- Não permite Pokémon sem treinador
- Nível mínimo do Pokémon é 1
- Batalha: nível maior vence; em empate de nível, tipo decide (Fogo > Planta > Água > Fogo)
- Pokémon não pode batalhar contra si mesmo

## Próximos passos

1. **Testar localmente** - Execute no terminal:
   ```
   uvicorn app.main:app --reload
   ```
   Acesse a documentação interativa em `http://localhost:8000/docs`

2. **Configurar Serverless** - Se quiser deploy na AWS Lambda, crie um `serverless.yml`

3. **Banco de dados real** - Substituir o banco em memória por SQLite, PostgreSQL ou DynamoDB

4. **Adicionar testes** - Criar testes unitários para validar os endpoints e regras de batalha

5. **Remover arquivo antigo** - O arquivo `requirements.py` pode ser deletado, pois foi criado o `requirements.txt` correto
