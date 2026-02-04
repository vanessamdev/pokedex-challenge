"""
Serviço de Batalhas.
Contém a lógica de negócio para simulação de batalhas entre pokémon.
"""
from fastapi import HTTPException
from app.models import BattleRequest, BattleResultVictory, BattleResultDraw, BattleWinner
from app.interfaces.database_interface import IDatabasePokemon


# Vantagens de tipo: chave vence valor
TYPE_ADVANTAGES = {
    "fogo": "planta",
    "planta": "agua",
    "agua": "fogo"
}


def _normalize_type(tipo: str) -> str:
    """Normaliza tipo para minúsculas sem acentos"""
    replacements = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ã": "a"}
    result = tipo.lower()
    for accented, plain in replacements.items():
        result = result.replace(accented, plain)
    return result


class BattleService:
    """Serviço responsável pelas batalhas entre Pokémon"""
    
    def __init__(self, pokemon_repo: IDatabasePokemon):
        self._pokemon_repo = pokemon_repo
    
    def battle(self, data: BattleRequest) -> BattleResultVictory | BattleResultDraw:
        """
        Simula uma batalha entre dois pokémon.
        
        Regras:
        1. Pokémon com nível maior vence
        2. Em empate de nível, tipo decide (Fogo > Planta > Água > Fogo)
        3. Se nível e tipo forem iguais, empate
        """
        # Validar: não pode batalhar contra si mesmo
        if data.pokemon_atacante_id == data.pokemon_defensor_id:
            raise HTTPException(
                status_code=400, 
                detail="Um Pokémon não pode batalhar contra ele mesmo"
            )
        
        # Buscar pokémon
        attacker = self._pokemon_repo.get(data.pokemon_atacante_id)
        defender = self._pokemon_repo.get(data.pokemon_defensor_id)
        
        # Validar existência
        if not attacker:
            raise HTTPException(status_code=404, detail="Pokémon atacante não encontrado")
        if not defender:
            raise HTTPException(status_code=404, detail="Pokémon defensor não encontrado")
        
        # Converter níveis (DynamoDB retorna Decimal)
        attacker_nivel = int(attacker["nivel"])
        defender_nivel = int(defender["nivel"])
        
        winner = None
        loser = None
        
        # Regra 1: Nível maior vence
        if attacker_nivel > defender_nivel:
            winner, loser = attacker, defender
        elif defender_nivel > attacker_nivel:
            winner, loser = defender, attacker
        else:
            # Regra 2: Vantagem de tipo
            attacker_type = _normalize_type(attacker["tipo"])
            defender_type = _normalize_type(defender["tipo"])
            
            if TYPE_ADVANTAGES.get(attacker_type) == defender_type:
                winner, loser = attacker, defender
            elif TYPE_ADVANTAGES.get(defender_type) == attacker_type:
                winner, loser = defender, attacker
            else:
                # Regra 3: Empate
                return BattleResultDraw()
        
        return BattleResultVictory(
            vencedor=BattleWinner(id=int(winner["id"]), nome=winner["nome"]),
            perdedor=BattleWinner(id=int(loser["id"]), nome=loser["nome"])
        )
