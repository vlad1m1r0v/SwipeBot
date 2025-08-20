from contextlib import suppress

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.api import (
    RequestContext,
    LoginScheme,
    RegisterScheme
)
from bot.database import Repository
from bot.states import (LoginStates, RegisterStates, MainStates)
from bot.utilities.validation import validate_password
from bot.keyboards import (
    get_login_enter_password_keyboard,
    get_main_menu_keyboard
)

router = Router()


@router.message(F.text == __("Submit"), RegisterStates.SUBMIT_MENU)
@router.message(F.text, LoginStates.ENTER_PASSWORD)
async def main_menu(message: Message, **kwargs):
    repository: Repository = kwargs.get("repository")

    state: FSMContext = kwargs.get("state")
    current_state = await state.get_state()

    if current_state == RegisterStates.SUBMIT_MENU:
        data = await state.get_data()

        register_data: RegisterScheme = RegisterScheme(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            password=data.get("password")
        )

        async with RequestContext(
                event=message,
                state=state,
                repository=repository
        ) as request:
            await request.register(data=register_data)

    elif current_state == LoginStates.ENTER_PASSWORD:
        if validate_password(message.text):
            await state.update_data({"password": message.text})

            data = await state.get_data()

            login_data: LoginScheme = LoginScheme(
                email=data.get("email"),
                password=data.get("password")
            )

            async with RequestContext(
                    event=message,
                    state=state,
                    repository=repository
            ) as request:
                await request.login(data=login_data)
        else:
            return await message.answer(
                text=_("Validation error. Please, enter password again:"),
                reply_markup=get_login_enter_password_keyboard()
            )

    await state.clear()
    await state.set_state(MainStates.MAIN_MENU)

    return await message.answer(
        text=_("Select action:"),
        reply_markup=get_main_menu_keyboard()
    )
