from dataclasses import asdict

from pymongo import AsyncMongoClient
from pymongo.results import InsertOneResult, UpdateResult

from bot.database.schemas import (
    GetUser,
    CreateUser,
    UpdateUser
)
from bot.utilities.dict import exclude_none_factory


class Repository:
    def __init__(self, mongo_uri: str):
        mongo_client = AsyncMongoClient(mongo_uri)
        database = mongo_client["database"]
        self._collection = database["users"]

    async def get_user(self, telegram_id: int) -> GetUser | None:
        return await self._collection.find_one({'telegram_id': telegram_id})

    async def create_user(self, data: CreateUser) -> InsertOneResult:
        return await self._collection.insert_one(asdict(data))

    async def update_user(self, telegram_id: int, data: UpdateUser) -> UpdateResult:
        return await self._collection.update_one(
            {"telegram_id": telegram_id},
            {"$set": asdict(data, dict_factory=exclude_none_factory)}
        )
