"""
Interface abstrata para operações de banco de dados.
Permite trocar implementação (memória/DynamoDB) sem alterar a lógica de negócio.
"""
from abc import ABC, abstractmethod
from typing import Optional


class IDatabaseTrainer(ABC):
    """Interface para operações de Treinador"""
    
    @abstractmethod
    def create(self, nome: str) -> dict:
        """Cria um novo treinador"""
        pass
    
    @abstractmethod
    def get(self, trainer_id: int) -> Optional[dict]:
        """Busca treinador por ID"""
        pass
    
    @abstractmethod
    def list_all(self) -> list[dict]:
        """Lista todos os treinadores"""
        pass
    
    @abstractmethod
    def update(self, trainer_id: int, nome: str) -> Optional[dict]:
        """Atualiza um treinador"""
        pass
    
    @abstractmethod
    def delete(self, trainer_id: int) -> bool:
        """Deleta um treinador"""
        pass


class IDatabasePokemon(ABC):
    """Interface para operações de Pokémon"""
    
    @abstractmethod
    def create(self, nome: str, tipo: str, nivel: int, treinador_id: int) -> dict:
        """Cria um novo pokémon"""
        pass
    
    @abstractmethod
    def get(self, pokemon_id: int) -> Optional[dict]:
        """Busca pokémon por ID"""
        pass
    
    @abstractmethod
    def list_all(self) -> list[dict]:
        """Lista todos os pokémon"""
        pass
    
    @abstractmethod
    def get_by_trainer(self, treinador_id: int) -> list[dict]:
        """Lista pokémon de um treinador"""
        pass
    
    @abstractmethod
    def update(self, pokemon_id: int, nome: str = None, tipo: str = None, nivel: int = None) -> Optional[dict]:
        """Atualiza um pokémon"""
        pass
    
    @abstractmethod
    def delete(self, pokemon_id: int) -> bool:
        """Deleta um pokémon"""
        pass
    
    @abstractmethod
    def delete_by_trainer(self, treinador_id: int) -> int:
        """Deleta todos os pokémon de um treinador"""
        pass
