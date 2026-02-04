"""
Configuração de Injeção de Dependências.
Centraliza a criação dos repositórios e serviços.
Seguindo o princípio D do SOLID (Dependency Inversion).
"""
import os
from functools import lru_cache

from app.interfaces.database_interface import IDatabaseTrainer, IDatabasePokemon
from app.repositories.memory_repository import MemoryTrainerRepository, MemoryPokemonRepository
from app.repositories.dynamodb_repository import DynamoDBTrainerRepository, DynamoDBPokemonRepository
from app.services.trainer_service import TrainerService
from app.services.pokemon_service import PokemonService
from app.services.battle_service import BattleService


# Configuração: usar DynamoDB ou memória
USE_DYNAMODB = os.environ.get("USE_DYNAMODB", "false").lower() == "true"


# Instâncias singleton dos repositórios
_trainer_repo: IDatabaseTrainer = None
_pokemon_repo: IDatabasePokemon = None


def get_trainer_repository() -> IDatabaseTrainer:
    """Retorna repositório de treinadores (singleton)"""
    global _trainer_repo
    if _trainer_repo is None:
        if USE_DYNAMODB:
            _trainer_repo = DynamoDBTrainerRepository()
        else:
            _trainer_repo = MemoryTrainerRepository()
    return _trainer_repo


def get_pokemon_repository() -> IDatabasePokemon:
    """Retorna repositório de pokémon (singleton)"""
    global _pokemon_repo
    if _pokemon_repo is None:
        if USE_DYNAMODB:
            _pokemon_repo = DynamoDBPokemonRepository()
        else:
            _pokemon_repo = MemoryPokemonRepository()
    return _pokemon_repo


def get_trainer_service() -> TrainerService:
    """Retorna serviço de treinadores"""
    return TrainerService(
        trainer_repo=get_trainer_repository(),
        pokemon_repo=get_pokemon_repository()
    )


def get_pokemon_service() -> PokemonService:
    """Retorna serviço de pokémon"""
    return PokemonService(
        pokemon_repo=get_pokemon_repository(),
        trainer_repo=get_trainer_repository()
    )


def get_battle_service() -> BattleService:
    """Retorna serviço de batalhas"""
    return BattleService(
        pokemon_repo=get_pokemon_repository()
    )
