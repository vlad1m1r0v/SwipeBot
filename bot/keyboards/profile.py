from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _

def get_profile_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("My announcements"))],
            [KeyboardButton(text=_("Profile information"))],
            [KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select option...")
    )

def get_profile_announcements_keyboard(limit: int, offset: int, total: int) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    nav_buttons_count = 0

    if offset > 0:
        builder.button(text=_("Previous"))
        nav_buttons_count += 1

    if offset + limit < total:
        builder.button(text=_("Next"))
        nav_buttons_count += 1

    builder.button(text=_("Back"))

    if nav_buttons_count > 0:
        builder.adjust(nav_buttons_count, 1)

    return builder.as_markup(resize_keyboard=True, input_field_placeholder=_("Select action..."))


def get_profile_information_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select action...")
    )