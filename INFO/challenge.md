# Desafio - API Pokédex

## Contexto

Somos uma empresa que está desenvolvendo uma plataforma simples de gerenciamento de Pokémon, inspirada no conceito de uma Pokédex, com o objetivo de organizar treinadores e seus Pokémon de forma prática e padronizada.

Precisamos de uma API REST que permita o cadastro e a consulta dessas informações, de forma simples, clara e bem estruturada, pois essa API servirá como base para futuras evoluções do sistema.

## Objetivo

Desenvolver uma API REST simples para gerenciar:
- Treinadores
- Pokémon
- A relação entre treinadores e seus Pokémon
- Funcionalidade extra que simule batalhas entre Pokémon

---

## Escopo Funcional

### 1. Treinadores

A API deve permitir:
- Cadastrar um treinador
- Listar todos os treinadores
- Buscar um treinador específico
- Atualizar os dados de um treinador
- Cada treinador deve possuir um ou mais Pokémon

### 2. Pokémon

A API deve permitir:
- Cadastrar um Pokémon
- Listar todos os Pokémon
- Buscar um Pokémon específico
- Atualizar os dados de um Pokémon
- Cada Pokémon deve pertencer a um único treinador
- Cada Pokémon deve conter apenas informações básicas (sem campos complexos)

### 3. Batalha de Pokémon (Funcionalidade Extra)

A API deve:
- Receber dois Pokémon
- Processar a batalha
- Retornar o vencedor ou empate
- Essa funcionalidade não precisa persistir histórico, apenas simular o resultado

---

## Regras de Negócio

- Um treinador pode ter um ou mais Pokémon
- Um Pokémon pertence a apenas um treinador
- Não deve ser possível cadastrar Pokémon sem treinador
- Não é permitido batalhar um Pokémon contra ele mesmo
- Apenas Pokémon existentes podem batalhar
- Nome do treinador é obrigatório
- Nome e tipo do Pokémon são obrigatórios
- Nível do Pokémon deve ser >= 1

### Regras da Batalha

- O Pokémon com nível mais alto vence
- Em caso de empate de nível:
  - Fogo vence Planta
  - Planta vence Água
  - Água vence Fogo
- Caso nível e tipo sejam iguais, o resultado é empate

---

## Requisitos Técnicos

- API REST
- Comunicação via JSON
- Uso adequado de HTTP Status Codes
- Estrutura simples e organizada
- Não é necessário autenticação
- Pode ser implementado em Node ou Python utilizando serverless framework

---

## Modelo de Dados

### Pokémon

| Campo | Tipo |
|-------|------|
| id | int |
| nome | str |
| tipo | str |
| nivel | int |
| treinador_id | int |

### Treinador

| Campo | Tipo |
|-------|------|
| id | int |
| nome | str |

---

## Endpoints - Treinadores

### Listar Treinadores

- Método: `GET`
- Endpoint: `/treinadores`
- Resposta (200):
```json
[
  {"id": 1, "nome": "Ash"},
  {"id": 2, "nome": "Misty"}
]
```

### Buscar um Treinador

- Método: `GET`
- Endpoint: `/treinadores/{id}`
- Resposta (200):
```json
{"id": 1, "nome": "Ash"}
```

### Cadastrar um Treinador

- Método: `POST`
- Endpoint: `/treinadores`
- Body:
```json
{"nome": "Brock"}
```
- Resposta (201):
```json
{"id": 3, "nome": "Brock"}
```

### Atualizar Treinador

- Método: `PUT`
- Endpoint: `/treinadores/{id}`
- Body:
```json
{"nome": "Ash Ketchum"}
```

---

## Endpoints - Pokémon

### Listar Pokémon

- Método: `GET`
- Endpoint: `/pokemons`
- Resposta (200):
```json
[
  {"id": 1, "nome": "Pikachu", "tipo": "Elétrico", "nivel": 10, "treinador_id": 1}
]
```

### Buscar um Pokémon

- Método: `GET`
- Endpoint: `/pokemons/{id}`

### Cadastrar Pokémon

- Método: `POST`
- Endpoint: `/pokemons`
- Body:
```json
{"nome": "Charmander", "tipo": "Fogo", "nivel": 8, "treinador_id": 1}
```
> ⚠️ O treinador_id deve existir.

### Atualizar Pokémon

- Método: `PUT`
- Endpoint: `/pokemons/{id}`
- Body:
```json
{"nome": "Charmander", "tipo": "Fogo", "nivel": 12}
```

---

## Relacionamento Treinador → Pokémon

### Listar Pokémon de um Treinador

- Descrição: Retorna todos os Pokémon de um treinador específico
- Método: `GET`
- Endpoint: `/treinadores/{id}/pokemons`
- Resposta (200):
```json
[
  {"id": 1, "nome": "Pikachu", "tipo": "Elétrico", "nivel": 10},
  {"id": 2, "nome": "Bulbasaur", "tipo": "Planta", "nivel": 7}
]
```

---

## Desafio Extra - Batalha de Pokémon

### Endpoint

- Método: `POST`
- Endpoint: `/batalhas`
- Body:
```json
{
  "pokemon_atacante_id": 1,
  "pokemon_defensor_id": 2
}
```

### Regras da Batalha

- O Pokémon com nível mais alto vence
- Se os níveis forem iguais, o tipo define o vencedor:
  - Fogo vence Planta
  - Planta vence Água
  - Água vence Fogo
- Se nível e tipo forem iguais, a batalha termina em empate
- Os dois Pokémon devem existir
- Não é permitido batalhar um Pokémon contra ele mesmo

### Resposta - Vitória

```json
{
  "resultado": "vitoria",
  "vencedor": {"id": 1, "nome": "Charmander"},
  "perdedor": {"id": 2, "nome": "Bulbasaur"}
}
```

### Resposta - Empate

```json
{
  "resultado": "empate",
  "mensagem": "Os Pokémon possuem força equivalente"
}
```
