"""
================================================================================
DESAFIO - API POKÉDEX
================================================================================

CONTEXTO
--------
Somos uma empresa que está desenvolvendo uma plataforma simples de gerenciamento 
de Pokémon, inspirada no conceito de uma Pokédex, com o objetivo de organizar 
treinadores e seus Pokémon de forma prática e padronizada.

Precisamos de uma API REST que permita o cadastro e a consulta dessas informações,
de forma simples, clara e bem estruturada, pois essa API servirá como base para 
futuras evoluções do sistema.

OBJETIVO
--------
Desenvolver uma API REST simples para gerenciar:
- Treinadores
- Pokémon
- A relação entre treinadores e seus Pokémon
- Funcionalidade extra que simule batalhas entre Pokémon

================================================================================
ESCOPO FUNCIONAL
================================================================================

1. TREINADORES
--------------
A API deve permitir:
- Cadastrar um treinador
- Listar todos os treinadores
- Buscar um treinador específico
- Atualizar os dados de um treinador
- Cada treinador deve possuir um ou mais Pokémon

2. POKÉMON
----------
A API deve permitir:
- Cadastrar um Pokémon
- Listar todos os Pokémon
- Buscar um Pokémon específico
- Atualizar os dados de um Pokémon
- Cada Pokémon deve pertencer a um único treinador
- Cada Pokémon deve conter apenas informações básicas (sem campos complexos)

3. BATALHA DE POKÉMON (Funcionalidade Extra)
--------------------------------------------
A API deve:
- Receber dois Pokémon
- Processar a batalha
- Retornar o vencedor ou empate
- Essa funcionalidade não precisa persistir histórico, apenas simular o resultado

================================================================================
REGRAS DE NEGÓCIO
================================================================================

- Um treinador pode ter um ou mais Pokémon
- Um Pokémon pertence a apenas um treinador
- Não deve ser possível cadastrar Pokémon sem treinador
- Não é permitido batalhar um Pokémon contra ele mesmo
- Apenas Pokémon existentes podem batalhar
- Nome do treinador é obrigatório
- Nome e tipo do Pokémon são obrigatórios
- Nível do Pokémon deve ser >= 1

REGRAS DA BATALHA
-----------------
- O Pokémon com nível mais alto vence
- Em caso de empate de nível:
    - Fogo vence Planta
    - Planta vence Água
    - Água vence Fogo
- Caso nível e tipo sejam iguais, o resultado é empate

================================================================================
REQUISITOS TÉCNICOS
================================================================================

- API REST
- Comunicação via JSON
- Uso adequado de HTTP Status Codes
- Estrutura simples e organizada
- Não é necessário autenticação
- Pode ser implementado em Node ou Python utilizando serverless framework

================================================================================
MODELO DE DADOS
================================================================================

POKÉMON:
- id: int
- nome: str
- tipo: str
- nivel: int
- treinador_id: int

TREINADOR:
- id: int
- nome: str

================================================================================
ENDPOINTS - TREINADORES
================================================================================

3.1 Listar Treinadores
----------------------
Método: GET
Endpoint: /treinadores
Resposta (200):
[
  {"id": 1, "nome": "Ash"},
  {"id": 2, "nome": "Misty"}
]

3.2 Buscar um Treinador
-----------------------
Método: GET
Endpoint: /treinadores/{id}
Resposta (200):
{"id": 1, "nome": "Ash"}

3.3 Cadastrar um Treinador
--------------------------
Método: POST
Endpoint: /treinadores
Body: {"nome": "Brock"}
Resposta (201):
{"id": 3, "nome": "Brock"}

3.4 Atualizar Treinador
-----------------------
Método: PUT
Endpoint: /treinadores/{id}
Body: {"nome": "Ash Ketchum"}

================================================================================
ENDPOINTS - POKÉMON
================================================================================

4.1 Listar Pokémon
------------------
Método: GET
Endpoint: /pokemons
Resposta (200):
[
  {"id": 1, "nome": "Pikachu", "tipo": "Elétrico", "nivel": 10, "treinador_id": 1}
]

4.2 Buscar um Pokémon
---------------------
Método: GET
Endpoint: /pokemons/{id}

4.3 Cadastrar Pokémon
---------------------
Método: POST
Endpoint: /pokemons
Body: {"nome": "Charmander", "tipo": "Fogo", "nivel": 8, "treinador_id": 1}
⚠️ O treinador_id deve existir.

4.4 Atualizar Pokémon
---------------------
Método: PUT
Endpoint: /pokemons/{id}
Body: {"nome": "Charmander", "tipo": "Fogo", "nivel": 12}

================================================================================
RELACIONAMENTO TREINADOR → POKÉMON
================================================================================

5.1 Listar Pokémon de um Treinador
----------------------------------
Descrição: Retorna todos os Pokémon de um treinador específico.
Método: GET
Endpoint: /treinadores/{id}/pokemons
Resposta (200):
[
  {"id": 1, "nome": "Pikachu", "tipo": "Elétrico", "nivel": 10},
  {"id": 2, "nome": "Bulbasaur", "tipo": "Planta", "nivel": 7}
]

================================================================================
DESAFIO EXTRA - BATALHA DE POKÉMON
================================================================================

ENDPOINT
--------
Método: POST
Endpoint: /batalhas
Body:
{
  "pokemon_atacante_id": 1,
  "pokemon_defensor_id": 2
}

REGRAS DA BATALHA
-----------------
- O Pokémon com nível mais alto vence
- Se os níveis forem iguais, o tipo define o vencedor:
    - Fogo vence Planta
    - Planta vence Água
    - Água vence Fogo
- Se nível e tipo forem iguais, a batalha termina em empate
- Os dois Pokémon devem existir
- Não é permitido batalhar um Pokémon contra ele mesmo

RESPOSTA - VITÓRIA
------------------
{
  "resultado": "vitoria",
  "vencedor": {"id": 1, "nome": "Charmander"},
  "perdedor": {"id": 2, "nome": "Bulbasaur"}
}

RESPOSTA - EMPATE
-----------------
{
  "resultado": "empate",
  "mensagem": "Os Pokémon possuem força equivalente"
}
"""
