from aiogram import Router, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.filters import FormCancelFilter
from bot.database import Repository
from bot.states import (
    StartStates,
    LanguageStates,
    RegisterStates,
    LoginStates,
    MainStates
)
from bot.keyboards import get_start_menu_keyboard

router = Router()


@router.message(CommandStart())
@router.message(F.text == __("Log out"), MainStates.MAIN_MENU)
@router.message(FormCancelFilter(LoginStates))
@router.message(FormCancelFilter(RegisterStates))
@router.message(F.text == __("Back"), LanguageStates.LANGUAGE_MENU)
async def start_menu(
        message: Message,
        state: FSMContext,
        repository: Repository,
):
    if message.text == _("Log out") and await state.get_state() == MainStates.MAIN_MENU:
        await repository.logout_user(message.from_user.id)

    await state.clear()
    await state.set_state(StartStates.START_MENU)

    return await message.answer(
        text=_("Welcome to the Swipe Bot.\nSelect one of the listed options below:"),
        reply_markup=get_start_menu_keyboard()
    )
