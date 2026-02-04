"""
Módulo de modelos Pydantic para validação de dados.
Define as estruturas de entrada e saída da API.
"""
from pydantic import BaseModel, Field
from typing import Optional

# ============ MODELOS DE TREINADOR ============

class TrainerCreate(BaseModel):
    """Dados para criar um novo treinador"""
    nome: str

class TrainerUpdate(BaseModel):
    """Dados para atualizar um treinador"""
    nome: str

class Trainer(BaseModel):
    """Representação completa de um treinador"""
    id: int
    nome: str

# ============ MODELOS DE POKÉMON ============

class PokemonCreate(BaseModel):
    """Dados para criar um novo pokémon"""
    nome: str
    tipo: str
    nivel: int = Field(ge=1, description="Nível mínimo é 1")
    treinador_id: int

class PokemonUpdate(BaseModel):
    """Dados para atualizar um pokémon (campos opcionais)"""
    nome: Optional[str] = None
    tipo: Optional[str] = None
    nivel: Optional[int] = Field(default=None, ge=1)

class Pokemon(BaseModel):
    """Representação completa de um pokémon"""
    id: int
    nome: str
    tipo: str
    nivel: int
    treinador_id: int

class PokemonSimple(BaseModel):
    """Pokémon sem referência ao treinador (para listagens)"""
    id: int
    nome: str
    tipo: str
    nivel: int

# ============ MODELOS DE BATALHA ============

class BattleRequest(BaseModel):
    """Dados para iniciar uma batalha"""
    pokemon_atacante_id: int
    pokemon_defensor_id: int

class BattleWinner(BaseModel):
    """Dados do pokémon vencedor/perdedor"""
    id: int
    nome: str

class BattleResultVictory(BaseModel):
    """Resultado de batalha com vencedor"""
    resultado: str = "vitoria"
    vencedor: BattleWinner
    perdedor: BattleWinner

class BattleResultDraw(BaseModel):
    """Resultado de batalha com empate"""
    resultado: str = "empate"
    mensagem: str = "Os Pokémon possuem força equivalente"
