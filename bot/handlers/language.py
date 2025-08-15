from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import I18n, gettext as _

from bot.database.repository import Repository
from bot.database.schemas import UpdateUser
from bot.states.auth import AuthStates
from bot.states.language import LanguageStates
from bot.keyboards.start import get_start_menu_keyboard
from bot.keyboards.language import get_language_keyboard
from bot.utilities.enums import Language


async def language_menu(message: Message, state: FSMContext):
    await state.set_state(LanguageStates.SWITCH_LANGUAGE)

    return await message.answer(
        text=_("Choose a language:"),
        reply_markup=get_language_keyboard()
    )


async def set_language(
        message: Message,
        repository: Repository,
        state: FSMContext,
):
    language_code = Language.EN if message.text == "English" else Language.UK

    await repository.update_user(
        telegram_id=message.from_user.id,
        data=UpdateUser(language=language_code)
    )

    await state.set_state(AuthStates.START)

    await message.answer(
        _("Language has been successfully changed.", locale=language_code),
        reply_markup=get_start_menu_keyboard(language_code)
    )


async def back_to_start(message: Message, state: FSMContext):
    await state.set_state(AuthStates.START)

    await message.answer(
        _("You have returned to the main menu."),
        reply_markup=get_start_menu_keyboard()
    )
