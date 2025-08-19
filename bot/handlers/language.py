from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.database import (Repository, UpdateUser)
from bot.states import (StartStates, LanguageStates)
from bot.keyboards import (get_language_menu_keyboard, get_start_menu_keyboard)
from bot.utilities.enums import Language

router = Router()


@router.message(F.text == __("Change language"), StartStates.START_MENU)
async def language_menu(message: Message, state: FSMContext):
    await state.set_state(LanguageStates.LANGUAGE_MENU)

    return await message.answer(
        text=_("Select a language:"),
        reply_markup=get_language_menu_keyboard()
    )


@router.message(F.text.in_({"English", "Українська"}), LanguageStates.LANGUAGE_MENU)
async def select_language(
        message: Message,
        repository: Repository,
        state: FSMContext,
):
    language_code = Language.EN if message.text == "English" else Language.UK

    await repository.update_user(
        telegram_id=message.from_user.id,
        data=UpdateUser(language=language_code)
    )

    await state.set_state(StartStates.START_MENU)

    await message.answer(
        _("Language has been successfully changed.", locale=language_code),
        reply_markup=get_start_menu_keyboard(language_code)
    )
