from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from bot.states.auth import AuthStates
from bot.keyboards.start import get_start_menu_keyboard


async def start_menu(message: Message, state: FSMContext):
    await state.set_state(AuthStates.START)

    return await message.answer(
        text=_("Welcome to the Swipe Bot.\nSelect one of the listed options below:"),
        reply_markup=get_start_menu_keyboard()
    )
