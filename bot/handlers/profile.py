import time
from datetime import datetime

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.api import (
    RequestContext,
    SuccessResponse,
    PaginatedResponse,
    GetAnnouncementSchema,
    GetUserSchema
)
from bot.database import Repository
from bot.states import (
    MainStates,
    UserStates
)
from bot.keyboards import (
    get_profile_menu_keyboard,
    get_profile_announcements_keyboard,
    get_profile_information_keyboard
)
from bot.utilities.pagination import MY_ANNOUNCEMENTS_PER_PAGE

router = Router()


@router.message(F.text == __("Back"), UserStates.PROFILE)
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

        reply_markup = get_profile_announcements_keyboard(
            limit=response["data"]["limit"],
            offset=response["data"]["offset"],
            total=response["data"]["total"]
        )

        if len(announcements) == 0:
            await message.answer(
                text=_("You have not created any announcements."),
                reply_markup=reply_markup
            )

        for (index, announcement) in enumerate(announcements):
            text = (
                f"{_('Price:')} {announcement['apartment'].get('price', _('Not available'))}\n"
                f"{_('Rooms:')} {announcement['apartment'].get('rooms', _('Not available'))}\n"
                f"{_('Area:')} {announcement['apartment'].get('area', _('Not available'))}\n"
                f"{_('Floor:')} {announcement['apartment'].get('floor_no', _('Not selected'))}\n"
                f"{_('Total floors:')} {announcement['apartment'].get('total_floors', _('Not selected'))}\n"
                f"{_('Address:')} {announcement['apartment'].get('address', _('Not available'))}\n"
            )

            photo_url = f"{announcement["apartment"]["preview_url"]}?cache_bust={int(time.time())}"

            if index + 1 < len(announcements):
                await message.answer_photo(
                    photo=photo_url,
                    caption=text
                )
            else:
                await message.answer_photo(
                    photo=photo_url,
                    caption=text,
                    reply_markup=reply_markup
                )


@router.message(F.text == __("Profile information"), UserStates.MENU)
async def profile_announcements(
        message: Message,
        repository: Repository,
        state: FSMContext
):
    await state.set_state(UserStates.PROFILE)

    async with RequestContext(
            event=message,
            state=state,
            repository=repository
    ) as request:
        response: SuccessResponse[GetUserSchema] = await request.get_profile()

        user = response["data"]

        expiry_date_str = datetime.strptime(
            user["subscription"]["expiry_date"].replace("Z", ""),
            "%Y-%m-%dT%H:%M:%S.%f"
        )
        formatted_expiry_date_str = expiry_date_str.strftime("%H:%M:%S %d.%m.%Y")

        text = (f"{_('<b>Account:</b>')}\n" +
                f"{_('Name:')} {user.get('name', _('Not entered'))}\n" +
                f"{_('Email:')} {user.get('email', _('Not entered'))}\n" +
                f"{_('Phone:')} {user.get('phone', _('Not entered'))}\n" +
                f"{_('<b>Contact:</b>')}\n" +
                f"{_('First name:')} {user.get('contact', {}).get('first_name', _('Not entered'))}\n" +
                f"{_('Last name:')} {user.get('contact', {}).get('last_name', _('Not entered'))}\n" +
                f"{_('Email:')} {user.get('contact', {}).get('email', _('Not entered'))}\n" +
                f"{_('Phone:')} {user.get('contact', {}).get('phone', _('Not entered'))}\n" +
                f"{_('<b>Agent contact:</b>')}\n" +
                f"{_('First name:')} {user.get('agent_contact', {}).get('first_name', _('Not entered'))}\n" +
                f"{_('Last name:')} {user.get('agent_contact', {}).get('last_name', _('Not entered'))}\n" +
                f"{_('Email:')} {user.get('agent_contact', {}).get('email', _('Not entered'))}\n" +
                f"{_('Phone:')} {user.get('agent_contact', {}).get('phone', _('Not entered'))}\n" +
                f"{_('<b>Balance:</b>')} {user.get('balance', {}).get('value', _('Not entered'))}\n" +
                f"{_('<b>Subscription:</b>')}\n" +
                f"{_('Autorenewal:')} {_('enabled') if user.get('subscription', {}).get('is_auto_renewal') else _('disabled')}\n" +
                f"{_('Expiry:')} {formatted_expiry_date_str}\n" +
                f"{_('<b>Notification settings:</b>')}\n" +
                f"{_('Redirect notifications to agent:')} {_('enabled') if user.get('notification_settings', {}).get('redirect_notifications_to_agent') else _('disabled')}\n" +
                f"{_('Send messages to:')} {user.get('notification_settings', {}).get('notification_type', _('Not entered'))}")

        photo_url = user.get("photo_url", None)

        if photo_url:
            await message.answer_photo(
                photo=f"{photo_url}?cache_bust={int(time.time())}",
                caption=text,
                reply_markup=get_profile_information_keyboard()
            )
        else:
            await message.answer(
                text=text,
                reply_markup=get_profile_information_keyboard()
            )
