import time

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
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
    MainStates,
    UserStates
)
from bot.keyboards import (
    get_profile_menu_keyboard,
    get_profile_announcements_keyboard
)
from bot.utilities.pagination import MY_ANNOUNCEMENTS_PER_PAGE

router = Router()


@router.message(F.text == __("Back"), UserStates.ANNOUNCEMENTS)
@router.message(F.text == __("Profile"), MainStates.MAIN_MENU)
async def profile_menu(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(UserStates.MENU)

    return await message.answer(
        text=_("Select action:"),
        reply_markup=get_profile_menu_keyboard()
    )

@router.message(F.text == __("Previous"), UserStates.ANNOUNCEMENTS)
@router.message(F.text == __("Next"), UserStates.ANNOUNCEMENTS)
@router.message(F.text == __("My announcements"), UserStates.MENU)
async def profile_announcements(
        message: Message,
        repository: Repository,
        state: FSMContext
):
    await state.set_state(UserStates.ANNOUNCEMENTS)

    data = await state.get_data()
    offset: int = data.get("offset", 0)

    notification_message = await message.answer(
        text=_(_("Loading your announcements...")),
        reply_markup=ReplyKeyboardRemove()
    )

    async with RequestContext(
            event=message,
            state=state,
            repository=repository
    ) as request:
        if message.text == _("Previous"):
            offset -= MY_ANNOUNCEMENTS_PER_PAGE
            await state.update_data({"offset": offset})

        if message.text == _("Next"):
            offset += MY_ANNOUNCEMENTS_PER_PAGE
            await state.update_data({"offset": offset})

        response: SuccessResponse[PaginatedResponse[GetAnnouncementSchema]] = \
            await request.get_my_announcements(offset=offset)

        await notification_message.delete()

        announcements = response["data"]["items"]

        for (index, announcement) in enumerate(announcements):
            text = (f"{_('Price:')} {announcement["apartment"]["price"]}\n" +
                    f"{_('Rooms:')} {announcement["apartment"]["rooms"]}\n" +
                    f"{_('Area:')} {announcement["apartment"]["area"]}\n" +
                    f"{_('Floor:')} {announcement["apartment"]["floor_no"] or "Not selected"}\n" +
                    f"{_('Total floors:')} {announcement["apartment"]["total_floors"] or "Not selected"}\n" +
                    f"{_('Address:')} {announcement["apartment"]["address"]}\n")

            photo_url = f"{announcement["apartment"]["preview_url"]}?cache_bust={int(time.time())}"

            if index + 1 < len(announcements):
                await message.answer_photo(
                    photo=photo_url,
                    caption=text
                )
            else:
                reply_markup = get_profile_announcements_keyboard(
                    limit=response["data"]["limit"],
                    offset=response["data"]["offset"],
                    total=response["data"]["total"]
                )

                await message.answer_photo(
                    photo=photo_url,
                    caption=text,
                    reply_markup=reply_markup
                )
