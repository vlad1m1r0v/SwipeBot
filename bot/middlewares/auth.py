from typing import Callable, Dict, Any, Awaitable, Union

from aiogram.utils.i18n import gettext as _
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.database.repository import Repository
from bot.database.schemas import GetUser, CreateUser
from bot.keyboards.start import get_start_menu_keyboard
from bot.states.auth import AuthStates, LoginStates, RegisterStates
from bot.states.language import LanguageStates


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

        user: GetUser | None = await repository.get_user(telegram_id)

        if bool(user) and bool(user.get("access_token")):
            return await handler(event, data)

        if user is None:
            await repository.create_user(CreateUser(telegram_id=telegram_id))

        is_authenticated = bool(user and user.get("access_token"))
        is_auth_state = current_state in [*AuthStates, *LanguageStates, *RegisterStates, *LoginStates]

        if not is_auth_state and not is_authenticated:
            await state.set_state(AuthStates.START)
            await event.answer(_("You are not authorized. Please, log in or register."))

            if isinstance(event, CallbackQuery):
                await event.message.answer(_("Select action:"), reply_markup=get_start_menu_keyboard())
            else:
                await event.answer(_("Select action:"), reply_markup=get_start_menu_keyboard())
        return await handler(event, data)