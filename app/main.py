"""
Módulo principal da API Pokédex.
Define os endpoints REST e configurações do FastAPI.

Deploy:
- Vercel: usa o app FastAPI diretamente via api/index.py
- AWS Lambda: usa o handler Mangum (comentado abaixo)
"""
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# ============ IMPORT AWS LAMBDA (comentado para Vercel) ============
# from mangum import Mangum

from app.models import (
    TrainerCreate, TrainerUpdate, Trainer,
    PokemonCreate, PokemonUpdate, Pokemon, PokemonSimple,
    BattleRequest, BattleResultVictory, BattleResultDraw
)
from app.services.trainer_service import TrainerService
from app.services.pokemon_service import PokemonService
from app.services.battle_service import BattleService
from app.dependencies import get_trainer_service, get_pokemon_service, get_battle_service


# Configuração do FastAPI
app = FastAPI(
    title="Pokédex API",
    description="API REST para gerenciamento de Treinadores e Pokémon",
    version="1.0.0"
)

# CORS - permite requisições do frontend
# Em produção na Vercel, frontend e backend estão no mesmo domínio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============ ENDPOINTS DE TREINADORES ============

@app.get("/treinadores", response_model=list[Trainer])
def list_trainers(service: TrainerService = Depends(get_trainer_service)):
    """Lista todos os treinadores"""
    return service.list_all()


@app.get("/treinadores/{trainer_id}", response_model=Trainer)
def get_trainer(trainer_id: int, service: TrainerService = Depends(get_trainer_service)):
    """Busca um treinador por ID"""
    return service.get_by_id(trainer_id)


@app.post("/treinadores", response_model=Trainer, status_code=201)
def create_trainer(data: TrainerCreate, service: TrainerService = Depends(get_trainer_service)):
    """Cria um novo treinador"""
    return service.create(data)


@app.put("/treinadores/{trainer_id}", response_model=Trainer)
def update_trainer(trainer_id: int, data: TrainerUpdate, service: TrainerService = Depends(get_trainer_service)):
    """Atualiza um treinador"""
    return service.update(trainer_id, data)


@app.delete("/treinadores/{trainer_id}", status_code=204)
def delete_trainer(trainer_id: int, service: TrainerService = Depends(get_trainer_service)):
    """Deleta um treinador e seus pokémon"""
    service.delete(trainer_id)
    return None


# ============ ENDPOINTS DE POKÉMON ============

@app.get("/pokemons", response_model=list[Pokemon])
def list_pokemons(service: PokemonService = Depends(get_pokemon_service)):
    """Lista todos os pokémon"""
    return service.list_all()


@app.get("/pokemons/{pokemon_id}", response_model=Pokemon)
def get_pokemon(pokemon_id: int, service: PokemonService = Depends(get_pokemon_service)):
    """Busca um pokémon por ID"""
    return service.get_by_id(pokemon_id)


@app.post("/pokemons", response_model=Pokemon, status_code=201)
def create_pokemon(data: PokemonCreate, service: PokemonService = Depends(get_pokemon_service)):
    """Cria um novo pokémon"""
    return service.create(data)


@app.put("/pokemons/{pokemon_id}", response_model=Pokemon)
def update_pokemon(pokemon_id: int, data: PokemonUpdate, service: PokemonService = Depends(get_pokemon_service)):
    """Atualiza um pokémon"""
    return service.update(pokemon_id, data)


@app.delete("/pokemons/{pokemon_id}", status_code=204)
def delete_pokemon(pokemon_id: int, service: PokemonService = Depends(get_pokemon_service)):
    """Deleta um pokémon"""
    service.delete(pokemon_id)
    return None


# ============ RELACIONAMENTO TREINADOR → POKÉMON ============

@app.get("/treinadores/{trainer_id}/pokemons", response_model=list[PokemonSimple])
def get_trainer_pokemons(trainer_id: int, service: PokemonService = Depends(get_pokemon_service)):
    """Lista todos os pokémon de um treinador"""
    return service.get_by_trainer(trainer_id)


# ============ ENDPOINT DE BATALHA ============

@app.post("/batalhas", response_model=BattleResultVictory | BattleResultDraw)
def battle(data: BattleRequest, service: BattleService = Depends(get_battle_service)):
    """Simula uma batalha entre dois pokémon"""
    return service.battle(data)


# ============ HANDLER AWS LAMBDA (comentado para Vercel) ============
# Descomente para deploy na AWS Lambda com Serverless Framework
# from mangum import Mangum
# handler = Mangum(app)
