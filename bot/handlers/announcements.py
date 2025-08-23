from typing import Union

import time

from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InputMediaPhoto,
    ReplyKeyboardRemove
)
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.api import (
    RequestContext,
    SuccessResponse,
    PaginatedResponse,
    GetAnnouncementSchema
)
from bot.database import Repository
from bot.states import (
    AnnouncementsStates,
    MainStates
)
from bot.keyboards import (
    get_announcements_feed_inline_keyboard,
    get_geo_inline_keyboard
)
from bot.callbacks import (
    PaginationCallback,
    GeolocationCallback,
    BackCallback,
)

router = Router()


@router.callback_query(BackCallback.filter(), AnnouncementsStates.GEO)
@router.callback_query(PaginationCallback.filter(), AnnouncementsStates.FEED)
@router.message(F.text == __("Announcements"), MainStates.MAIN_MENU)
async def announcements_feed(
        event: Union[Message, CallbackQuery],
        repository: Repository,
        state: FSMContext,
        **kwargs
):
    await state.set_state(AnnouncementsStates.FEED)
    data = await state.get_data()
    callback_data = kwargs.get("callback_data", {})
    offset = data.get("offset", 0)

    if isinstance(event, CallbackQuery) and isinstance(callback_data, PaginationCallback):
            offset = callback_data.offset
            await state.update_data({"offset": offset})

    async with RequestContext(
            event=event,
            state=state,
            repository=repository
    ) as request:
        response: SuccessResponse[PaginatedResponse[GetAnnouncementSchema]] = \
            await request.get_announcements(offset=offset)

        announcement = response["data"]["items"][0]

        text = (
            f"{_('Price:')} {announcement['apartment'].get('price', _('Not available'))}\n"
            f"{_('Rooms:')} {announcement['apartment'].get('rooms', _('Not available'))}\n"
            f"{_('Area:')} {announcement['apartment'].get('area', _('Not available'))}\n"
            f"{_('Floor:')} {announcement['apartment'].get('floor_no', _('Not selected'))}\n"
            f"{_('Total floors:')} {announcement['apartment'].get('total_floors', _('Not selected'))}\n"
            f"{_('Address:')} {announcement['apartment'].get('address', _('Not available'))}\n"
        )

        photo_url = f"{announcement["apartment"]["preview_url"]}?cache_bust={int(time.time())}"

        reply_markup = get_announcements_feed_inline_keyboard(
            limit=response["data"]["limit"],
            offset=response["data"]["offset"],
            total=response["data"]["total"],
            longitude=announcement["apartment"]["longitude"],
            latitude=announcement["apartment"]["latitude"],
        )

        if isinstance(event, Message):
            message = await event.answer(
                text=_("Updating..."),
                reply_markup=ReplyKeyboardRemove()
            )

            await message.delete()

            await event.answer_photo(
                photo=photo_url,
                caption=text,
                reply_markup=reply_markup
            )
        elif isinstance(event, CallbackQuery) and isinstance(callback_data, BackCallback):
            await event.message.answer_photo(
                photo=photo_url,
                caption=text,
                reply_markup=reply_markup
            )

            await event.message.delete()
        else:
            new_media = InputMediaPhoto(
                media=photo_url,
                caption=text
            )
            await event.message.edit_media(media=new_media, reply_markup=reply_markup)


@router.callback_query(GeolocationCallback.filter(), AnnouncementsStates.FEED)
async def show_geolocation(
        query: CallbackQuery,
        callback_data: GeolocationCallback,
        state: FSMContext,
):
    await state.set_state(AnnouncementsStates.GEO)

    await query.message.delete()

    await query.message.answer_location(
        latitude=callback_data.latitude,
        longitude=callback_data.longitude,
        reply_markup=get_geo_inline_keyboard()
    )
