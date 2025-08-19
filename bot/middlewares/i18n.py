from aiogram.utils.i18n import I18n, I18nMiddleware
from typing import Dict, Any
from aiogram.types import TelegramObject

from bot.database import (Repository, GetUser)
from bot.utilities.enums import Language


class CustomI18nMiddleware(I18nMiddleware):
    def __init__(self, i18n: I18n):
        super().__init__(i18n)

    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        repository: Repository = data["repository"]

        user: GetUser = await repository.get_user(event.from_user.id)

        if user and user.get("language"):
            return user.get("language")

        return Language.EN
