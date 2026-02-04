"""
Serviço de Treinadores.
Contém a lógica de negócio para operações com treinadores.
"""
from fastapi import HTTPException
from app.models import TrainerCreate, TrainerUpdate, Trainer
from app.interfaces.database_interface import IDatabaseTrainer, IDatabasePokemon


class TrainerService:
    """Serviço responsável pelas operações de Treinador"""
    
    def __init__(self, trainer_repo: IDatabaseTrainer, pokemon_repo: IDatabasePokemon):
        self._trainer_repo = trainer_repo
        self._pokemon_repo = pokemon_repo
    
    def list_all(self) -> list[Trainer]:
        """Lista todos os treinadores"""
        trainers = self._trainer_repo.list_all()
        return [Trainer(id=int(t["id"]), nome=t["nome"]) for t in trainers]
    
    def get_by_id(self, trainer_id: int) -> Trainer:
        """Busca treinador por ID"""
        trainer = self._trainer_repo.get(trainer_id)
        if not trainer:
            raise HTTPException(status_code=404, detail="Treinador não encontrado")
        return Trainer(id=int(trainer["id"]), nome=trainer["nome"])
    
    def create(self, data: TrainerCreate) -> Trainer:
        """Cria um novo treinador"""
        trainer = self._trainer_repo.create(data.nome)
        return Trainer(id=int(trainer["id"]), nome=trainer["nome"])
    
    def update(self, trainer_id: int, data: TrainerUpdate) -> Trainer:
        """Atualiza um treinador"""
        trainer = self._trainer_repo.update(trainer_id, data.nome)
        if not trainer:
            raise HTTPException(status_code=404, detail="Treinador não encontrado")
        return Trainer(id=int(trainer["id"]), nome=trainer["nome"])
    
    def delete(self, trainer_id: int) -> bool:
        """Deleta treinador e seus pokémon"""
        trainer = self._trainer_repo.get(trainer_id)
        if not trainer:
            raise HTTPException(status_code=404, detail="Treinador não encontrado")
        
        # Deletar pokémon do treinador primeiro (integridade referencial)
        self._pokemon_repo.delete_by_trainer(trainer_id)
        
        # Deletar treinador
        self._trainer_repo.delete(trainer_id)
        return True
    
    def exists(self, trainer_id: int) -> bool:
        """Verifica se treinador existe"""
        return self._trainer_repo.get(trainer_id) is not None
