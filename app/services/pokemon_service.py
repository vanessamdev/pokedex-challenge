"""
Serviço de Pokémon.
Contém a lógica de negócio para operações com pokémon.
"""
from fastapi import HTTPException
from app.models import PokemonCreate, PokemonUpdate, Pokemon, PokemonSimple
from app.interfaces.database_interface import IDatabaseTrainer, IDatabasePokemon


class PokemonService:
    """Serviço responsável pelas operações de Pokémon"""
    
    def __init__(self, pokemon_repo: IDatabasePokemon, trainer_repo: IDatabaseTrainer):
        self._pokemon_repo = pokemon_repo
        self._trainer_repo = trainer_repo
    
    def list_all(self) -> list[Pokemon]:
        """Lista todos os pokémon"""
        pokemons = self._pokemon_repo.list_all()
        return [Pokemon(
            id=int(p["id"]),
            nome=p["nome"],
            tipo=p["tipo"],
            nivel=int(p["nivel"]),
            treinador_id=int(p["treinador_id"])
        ) for p in pokemons]
    
    def get_by_id(self, pokemon_id: int) -> Pokemon:
        """Busca pokémon por ID"""
        pokemon = self._pokemon_repo.get(pokemon_id)
        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokémon não encontrado")
        return Pokemon(
            id=int(pokemon["id"]),
            nome=pokemon["nome"],
            tipo=pokemon["tipo"],
            nivel=int(pokemon["nivel"]),
            treinador_id=int(pokemon["treinador_id"])
        )
    
    def get_by_trainer(self, trainer_id: int) -> list[PokemonSimple]:
        """Lista pokémon de um treinador"""
        # Verificar se treinador existe
        if not self._trainer_repo.get(trainer_id):
            raise HTTPException(status_code=404, detail="Treinador não encontrado")
        
        pokemons = self._pokemon_repo.get_by_trainer(trainer_id)
        return [PokemonSimple(
            id=int(p["id"]),
            nome=p["nome"],
            tipo=p["tipo"],
            nivel=int(p["nivel"])
        ) for p in pokemons]
    
    def create(self, data: PokemonCreate) -> Pokemon:
        """Cria um novo pokémon"""
        # Validar se treinador existe
        if not self._trainer_repo.get(data.treinador_id):
            raise HTTPException(status_code=400, detail="Treinador não encontrado")
        
        pokemon = self._pokemon_repo.create(data.nome, data.tipo, data.nivel, data.treinador_id)
        return Pokemon(
            id=int(pokemon["id"]),
            nome=pokemon["nome"],
            tipo=pokemon["tipo"],
            nivel=int(pokemon["nivel"]),
            treinador_id=int(pokemon["treinador_id"])
        )
    
    def update(self, pokemon_id: int, data: PokemonUpdate) -> Pokemon:
        """Atualiza um pokémon"""
        pokemon = self._pokemon_repo.update(pokemon_id, data.nome, data.tipo, data.nivel)
        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokémon não encontrado")
        return Pokemon(
            id=int(pokemon["id"]),
            nome=pokemon["nome"],
            tipo=pokemon["tipo"],
            nivel=int(pokemon["nivel"]),
            treinador_id=int(pokemon["treinador_id"])
        )
    
    def delete(self, pokemon_id: int) -> bool:
        """Deleta um pokémon"""
        if not self._pokemon_repo.get(pokemon_id):
            raise HTTPException(status_code=404, detail="Pokémon não encontrado")
        self._pokemon_repo.delete(pokemon_id)
        return True
    
    def get_raw(self, pokemon_id: int) -> dict | None:
        """Retorna dados brutos do pokémon (para batalhas)"""
        return self._pokemon_repo.get(pokemon_id)
