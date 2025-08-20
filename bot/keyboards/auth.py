from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _


def get_login_enter_email_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter email...")
    )


def get_login_enter_password_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter password...")
    )


def get_register_enter_name_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter name...")
    )


def get_register_enter_email_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter email...")
    )


def get_register_enter_phone_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter phone...")
    )


def get_register_enter_password_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter password...")
    )


def get_register_submit_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Edit name"))],
            [KeyboardButton(text=_("Edit email"))],
            [KeyboardButton(text=_("Edit phone"))],
            [KeyboardButton(text=_("Edit password"))],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Submit"))],

        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select action...")
    )


def get_register_edit_name_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Edit name...")
    )


def get_register_edit_email_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Edit email...")
    )


def get_register_edit_phone_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Edit phone...")
    )


def get_register_edit_password_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Edit password...")
    )
