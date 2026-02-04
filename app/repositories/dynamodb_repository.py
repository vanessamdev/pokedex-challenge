"""
Repositório DynamoDB para produção na AWS.
Implementa as interfaces de banco de dados usando Amazon DynamoDB.
Os dados são persistidos permanentemente.
"""
import boto3
import os
from typing import Optional
from botocore.exceptions import ClientError
from app.interfaces.database_interface import IDatabaseTrainer, IDatabasePokemon


# Configuração do DynamoDB
REGION = os.environ.get("AWS_REGION", "us-east-1")
STAGE = os.environ.get("STAGE", "dev")
ENDPOINT_URL = os.environ.get("DYNAMODB_ENDPOINT", None)

# Nomes das tabelas
TRAINERS_TABLE = f"pokedex-trainers-{STAGE}"
POKEMONS_TABLE = f"pokedex-pokemons-{STAGE}"
COUNTERS_TABLE = f"pokedex-counters-{STAGE}"


def _get_dynamodb_resource():
    """Retorna recurso DynamoDB (local ou AWS)"""
    if ENDPOINT_URL:
        return boto3.resource("dynamodb", region_name=REGION, endpoint_url=ENDPOINT_URL)
    return boto3.resource("dynamodb", region_name=REGION)


def _get_next_id(entity: str) -> int:
    """Gera próximo ID usando contador atômico no DynamoDB"""
    dynamodb = _get_dynamodb_resource()
    table = dynamodb.Table(COUNTERS_TABLE)
    
    response = table.update_item(
        Key={"entity": entity},
        UpdateExpression="SET current_id = if_not_exists(current_id, :start) + :inc",
        ExpressionAttributeValues={":start": 0, ":inc": 1},
        ReturnValues="UPDATED_NEW"
    )
    return int(response["Attributes"]["current_id"])


class DynamoDBTrainerRepository(IDatabaseTrainer):
    """Repositório de Treinadores no DynamoDB"""
    
    def __init__(self):
        self._dynamodb = _get_dynamodb_resource()
        self._table = self._dynamodb.Table(TRAINERS_TABLE)
    
    def create(self, nome: str) -> dict:
        """Cria um novo treinador"""
        trainer_id = _get_next_id("trainer")
        item = {"id": trainer_id, "nome": nome}
        self._table.put_item(Item=item)
        return item
    
    def get(self, trainer_id: int) -> Optional[dict]:
        """Busca treinador por ID"""
        response = self._table.get_item(Key={"id": trainer_id})
        return response.get("Item")
    
    def list_all(self) -> list[dict]:
        """Lista todos os treinadores"""
        response = self._table.scan()
        return response.get("Items", [])
    
    def update(self, trainer_id: int, nome: str) -> Optional[dict]:
        """Atualiza um treinador"""
        try:
            response = self._table.update_item(
                Key={"id": trainer_id},
                UpdateExpression="SET nome = :nome",
                ExpressionAttributeValues={":nome": nome},
                ConditionExpression="attribute_exists(id)",
                ReturnValues="ALL_NEW"
            )
            return response.get("Attributes")
        except ClientError as e:
            if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
                return None
            raise
    
    def delete(self, trainer_id: int) -> bool:
        """Deleta um treinador"""
        try:
            self._table.delete_item(
                Key={"id": trainer_id},
                ConditionExpression="attribute_exists(id)"
            )
            return True
        except ClientError as e:
            if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
                return False
            raise


class DynamoDBPokemonRepository(IDatabasePokemon):
    """Repositório de Pokémon no DynamoDB"""
    
    def __init__(self):
        self._dynamodb = _get_dynamodb_resource()
        self._table = self._dynamodb.Table(POKEMONS_TABLE)
    
    def create(self, nome: str, tipo: str, nivel: int, treinador_id: int) -> dict:
        """Cria um novo pokémon"""
        pokemon_id = _get_next_id("pokemon")
        item = {
            "id": pokemon_id,
            "nome": nome,
            "tipo": tipo,
            "nivel": nivel,
            "treinador_id": treinador_id
        }
        self._table.put_item(Item=item)
        return item
    
    def get(self, pokemon_id: int) -> Optional[dict]:
        """Busca pokémon por ID"""
        response = self._table.get_item(Key={"id": pokemon_id})
        return response.get("Item")
    
    def list_all(self) -> list[dict]:
        """Lista todos os pokémon"""
        response = self._table.scan()
        return response.get("Items", [])
    
    def get_by_trainer(self, treinador_id: int) -> list[dict]:
        """Lista pokémon de um treinador"""
        response = self._table.scan(
            FilterExpression="treinador_id = :tid",
            ExpressionAttributeValues={":tid": treinador_id}
        )
        return response.get("Items", [])
    
    def update(self, pokemon_id: int, nome: str = None, tipo: str = None, nivel: int = None) -> Optional[dict]:
        """Atualiza um pokémon"""
        update_parts = []
        values = {}
        
        if nome is not None:
            update_parts.append("nome = :nome")
            values[":nome"] = nome
        if tipo is not None:
            update_parts.append("tipo = :tipo")
            values[":tipo"] = tipo
        if nivel is not None:
            update_parts.append("nivel = :nivel")
            values[":nivel"] = nivel
        
        if not update_parts:
            return self.get(pokemon_id)
        
        try:
            response = self._table.update_item(
                Key={"id": pokemon_id},
                UpdateExpression="SET " + ", ".join(update_parts),
                ExpressionAttributeValues=values,
                ConditionExpression="attribute_exists(id)",
                ReturnValues="ALL_NEW"
            )
            return response.get("Attributes")
        except ClientError as e:
            if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
                return None
            raise
    
    def delete(self, pokemon_id: int) -> bool:
        """Deleta um pokémon"""
        try:
            self._table.delete_item(
                Key={"id": pokemon_id},
                ConditionExpression="attribute_exists(id)"
            )
            return True
        except ClientError as e:
            if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
                return False
            raise
    
    def delete_by_trainer(self, treinador_id: int) -> int:
        """Deleta todos os pokémon de um treinador"""
        pokemons = self.get_by_trainer(treinador_id)
        count = 0
        for pokemon in pokemons:
            if self.delete(int(pokemon["id"])):
                count += 1
        return count
