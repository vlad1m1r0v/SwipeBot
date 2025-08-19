from typing import Callable, Dict, Any, Awaitable, Union

from aiogram.utils.i18n import gettext as _
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.database import (Repository, GetUser, CreateUser)
from bot.keyboards import get_start_menu_keyboard
from bot.states import (StartStates, LanguageStates, LoginStates, RegisterStates)


class AuthMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        telegram_id = event.from_user.id

        repository: Repository = data.get("repository")

        state: FSMContext = data.get("state")
        current_state = await state.get_state()
        is_auth_state = current_state in [
            *StartStates,
            *LanguageStates,
            *RegisterStates,
            *LoginStates
        ]

        if is_auth_state:
            return await handler(event, data)

        user: GetUser | None = await repository.get_user(telegram_id)

        if user is None:
            await repository.create_user(CreateUser(telegram_id=telegram_id))

        is_authenticated = bool(user and user.get("access_token"))

        if not is_authenticated:
            await state.set_state(StartStates.START_MENU)
            text = _("You are not authorized. Please, log in or register.")

            if isinstance(event, CallbackQuery):
                return await event.message.answer(text=text, reply_markup=get_start_menu_keyboard())
            else:
                return await event.answer(text=text, reply_markup=get_start_menu_keyboard())
        return await handler(event, data)
