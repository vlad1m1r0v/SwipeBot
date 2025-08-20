from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _


def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Announcements"))],
            [KeyboardButton(text=_("Profile"))],
            [KeyboardButton(text=_("Create announcement"))],
            [KeyboardButton(text=_("Log out"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select action...")
    )
