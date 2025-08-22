from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardButton
)
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.i18n import gettext as _

from bot.callbacks import (
    BackCallback,
    GeolocationCallback,
    PaginationCallback
)


def get_announcements_feed_inline_keyboard(
        limit: int,
        offset: int,
        total: int,
        longitude: float,
        latitude: float,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=_("Show geolocation"),
        callback_data=GeolocationCallback(longitude=longitude, latitude=latitude)
    )

    nav_buttons_count = 0

    if offset > 0:
        builder.button(
            text=_("Previous"),
            callback_data=PaginationCallback(offset=offset - limit)
        )
        nav_buttons_count += 1

    if offset + limit < total:
        builder.button(
            text=_("Next"),
            callback_data=PaginationCallback(offset=offset + limit)
        )
        nav_buttons_count += 1

    builder.button(text=_("Back"), callback_data=BackCallback())

    builder.adjust(1, nav_buttons_count, 1)

    return builder.as_markup()


def get_geo_inline_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=_("Back"),
        callback_data=BackCallback()
    )

    return builder.as_markup()
