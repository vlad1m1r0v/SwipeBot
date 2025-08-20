from aiogram import Router, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

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
@router.message(F.text == __("Back"), LoginStates.ENTER_EMAIL)
@router.message(F.text == __("Cancel"), LoginStates.ENTER_EMAIL)
@router.message(F.text == __("Cancel"), LoginStates.ENTER_PASSWORD)
@router.message(F.text == __("Back"), RegisterStates.ENTER_NAME)
@router.message(F.text == __("Cancel"), RegisterStates.ENTER_NAME)
@router.message(F.text == __("Cancel"), RegisterStates.ENTER_EMAIL)
@router.message(F.text == __("Cancel"), RegisterStates.ENTER_PHONE)
@router.message(F.text == __("Cancel"), RegisterStates.ENTER_PASSWORD)
@router.message(F.text == __("Cancel"), RegisterStates.SUBMIT_MENU)
@router.message(F.text == __("Back"), LanguageStates.LANGUAGE_MENU)
async def start_menu(
        message: Message,
        state: FSMContext
):
    await state.clear()
    await state.set_state(StartStates.START_MENU)

    return await message.answer(
        text=_("Welcome to the Swipe Bot.\nSelect one of the listed options below:"),
        reply_markup=get_start_menu_keyboard()
    )
