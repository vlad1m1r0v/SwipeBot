from typing import Union

from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InputMediaPhoto
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
    PaginationCallback
)

router = Router()


@router.callback_query(PaginationCallback.filter(), AnnouncementsStates.ANNOUNCEMENTS_FEED)
@router.message(F.text == __("Announcements"), MainStates.MAIN_MENU)
async def announcements_feed(
        event: Union[Message, CallbackQuery],
        repository: Repository,
        state: FSMContext,
        **kwargs
):
    await state.set_state(AnnouncementsStates.ANNOUNCEMENTS_FEED)
    data = await state.get_data()

    offset = data.get("offset", 0)

    if isinstance(event, CallbackQuery):
        callback_data: PaginationCallback = kwargs.get("callback_data")
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

        text = (f"{_('Price:')} {announcement["apartment"]["price"]}\n" +
                f"{_('Rooms:')} {announcement["apartment"]["rooms"]}\n" +
                f"{_('Area:')} {announcement["apartment"]["area"]}\n" +
                f"{_('Floor:')} {announcement["apartment"]["floor_no"]}\n" +
                f"{_('Total floors:')} {announcement["apartment"]["total_floors"]}\n" +
                f"{_('Address:')} {announcement["apartment"]["address"]}\n")

        photo_url = announcement["apartment"]["preview_url"]

        reply_markup = get_announcements_feed_inline_keyboard(
            limit=response["data"]["limit"],
            offset=response["data"]["offset"],
            total=response["data"]["total"],
            longitude=announcement["apartment"]["longitude"],
            latitude=announcement["apartment"]["latitude"],
        )

        if isinstance(event, Message):
            await event.answer_photo(
                photo=photo_url,
                caption=text,
                reply_markup=reply_markup
            )
        else:
            new_media = InputMediaPhoto(
                media=photo_url,
                caption=text
            )
            await event.message.edit_media(media=new_media, reply_markup=reply_markup)
