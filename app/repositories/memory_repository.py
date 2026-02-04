"""
Repositório em memória para desenvolvimento local.
Implementa as interfaces de banco de dados usando dicionários Python.
Os dados são perdidos ao reiniciar o servidor.
"""
from typing import Optional
from app.interfaces.database_interface import IDatabaseTrainer, IDatabasePokemon


class MemoryTrainerRepository(IDatabaseTrainer):
    """Repositório de Treinadores em memória"""
    
    def __init__(self):
        self._db: dict[int, dict] = {}
        self._counter = 0
    
    def _get_next_id(self) -> int:
        """Gera próximo ID único"""
        self._counter += 1
        return self._counter
    
    def create(self, nome: str) -> dict:
        """Cria um novo treinador"""
        new_id = self._get_next_id()
        item = {"id": new_id, "nome": nome}
        self._db[new_id] = item
        return item
    
    def get(self, trainer_id: int) -> Optional[dict]:
        """Busca treinador por ID"""
        return self._db.get(trainer_id)
    
    def list_all(self) -> list[dict]:
        """Lista todos os treinadores"""
        return list(self._db.values())
    
    def update(self, trainer_id: int, nome: str) -> Optional[dict]:
        """Atualiza um treinador"""
        if trainer_id not in self._db:
            return None
        self._db[trainer_id]["nome"] = nome
        return self._db[trainer_id]
    
    def delete(self, trainer_id: int) -> bool:
        """Deleta um treinador"""
        if trainer_id not in self._db:
            return False
        del self._db[trainer_id]
        return True


class MemoryPokemonRepository(IDatabasePokemon):
    """Repositório de Pokémon em memória"""
    
    def __init__(self):
        self._db: dict[int, dict] = {}
        self._counter = 0
    
    def _get_next_id(self) -> int:
        """Gera próximo ID único"""
        self._counter += 1
        return self._counter
    
    def create(self, nome: str, tipo: str, nivel: int, treinador_id: int) -> dict:
        """Cria um novo pokémon"""
        new_id = self._get_next_id()
        item = {
            "id": new_id,
            "nome": nome,
            "tipo": tipo,
            "nivel": nivel,
            "treinador_id": treinador_id
        }
        self._db[new_id] = item
        return item
    
    def get(self, pokemon_id: int) -> Optional[dict]:
        """Busca pokémon por ID"""
        return self._db.get(pokemon_id)
    
    def list_all(self) -> list[dict]:
        """Lista todos os pokémon"""
        return list(self._db.values())
    
    def get_by_trainer(self, treinador_id: int) -> list[dict]:
        """Lista pokémon de um treinador"""
        return [p for p in self._db.values() if p["treinador_id"] == treinador_id]
    
    def update(self, pokemon_id: int, nome: str = None, tipo: str = None, nivel: int = None) -> Optional[dict]:
        """Atualiza um pokémon"""
        if pokemon_id not in self._db:
            return None
        pokemon = self._db[pokemon_id]
        if nome is not None:
            pokemon["nome"] = nome
        if tipo is not None:
            pokemon["tipo"] = tipo
        if nivel is not None:
            pokemon["nivel"] = nivel
        return pokemon
    
    def delete(self, pokemon_id: int) -> bool:
        """Deleta um pokémon"""
        if pokemon_id not in self._db:
            return False
        del self._db[pokemon_id]
        return True
    
    def delete_by_trainer(self, treinador_id: int) -> int:
        """Deleta todos os pokémon de um treinador"""
        to_delete = [pid for pid, p in self._db.items() if p["treinador_id"] == treinador_id]
        for pid in to_delete:
            del self._db[pid]
        return len(to_delete)
