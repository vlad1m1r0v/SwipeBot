from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.i18n import gettext as _


class GeolocationCallback(CallbackData, prefix="geo"):
    longitude: float
    latitude: float


class PaginationCallback(CallbackData, prefix="page"):
    offset: int


class BackCallback(CallbackData, prefix="back"):
    pass


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
