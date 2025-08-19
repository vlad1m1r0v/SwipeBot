from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _


def get_language_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("English")), KeyboardButton(text=_("Українська"))],
            [KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select language...")
    )