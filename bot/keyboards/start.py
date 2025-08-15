from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _


def get_start_menu_keyboard(locale: str | None = None) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Login", locale=locale))],
            [KeyboardButton(text=_("Register", locale=locale))],
            [KeyboardButton(text=_("Change language", locale=locale))]
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select action...", locale=locale)
    )
