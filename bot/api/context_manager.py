import os

from typing import Union

from httpx import (Response, HTTPStatusError)

from aiogram.fsm.context import FSMContext
from aiogram.types import (Message, CallbackQuery)
from aiogram.utils.i18n import gettext as _

from .client import APIClient
from .schemas import ErrorResponse

from bot.database import Repository
from bot.states import StartStates
from bot.keyboards import get_start_menu_keyboard


class RequestContext:
    def __init__(
            self,
            event: Union[Message, CallbackQuery],
            state: FSMContext,
            repository: Repository,

    ):
        self.__event = event
        self.__state = state
        self.__repository = repository

    async def __aenter__(self):
        return APIClient(
            server_url=os.getenv("API_URI"),
            repository=self.__repository,
            telegram_id=self.__event.from_user.id or self.__event.mesage.from_user.id
        )

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return True

        if exc_type is HTTPStatusError:
            response: Response = exc_val.response

            if response.status_code in [400, 401, 403, 404]:
                await self.__state.set_state(StartStates.START_MENU)
                text = _("You are not authorized. Please, log in or register.")

                if isinstance(self.__event, CallbackQuery):
                    await self.__event.message.answer(text=text, reply_markup=get_start_menu_keyboard())
                else:
                    await self.__event.answer(text=text, reply_markup=get_start_menu_keyboard())

                return False

            else:
                error_response: ErrorResponse = response.json()
                error_details = error_response.get("error", {})
                error_code = error_details.get("code", "UNKNOWN_ERROR")
                error_message = error_details.get("details", {}).get("message", "No message provided.")

                text = _("An error occurred: {error_code}\nDetails: {error_message}").format(
                    error_code=error_code,
                    error_message=error_message
                )

                if isinstance(self.__event, CallbackQuery):
                    await self.__event.message.answer(text=text)
                else:
                    await self.__event.answer(text=text)

                return False

        else:
            text = _("An unexpected error occurred.")

            if isinstance(self.__event, CallbackQuery):
                await self.__event.message.answer(text=text)
            else:
                await self.__event.answer(text=text)

            return False
