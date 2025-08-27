from typing import Union

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.filters import FormCancelFilter
from bot.api import (
    RequestContext,
    LoginScheme,
    RegisterScheme,
    Base64Item,
    Action,
    Rooms,
    Commission,
    CreateApartmentSchema,
    CreateAnnouncementSchema,
    IDResponseSchema,
    SuccessResponse,
)
from bot.database import Repository
from bot.states import (
    LoginStates,
    RegisterStates,
    MainStates,
    AnnouncementsStates,
    UserStates,
    AnnouncementCreationStates
)
from bot.utilities.validation import validate_password
from bot.utilities.format import format_viewing_time
from bot.utilities.file_id_to_base64 import file_id_to_base64
from bot.keyboards import (
    get_login_enter_password_keyboard,
    get_main_menu_keyboard
)
from bot.callbacks import BackCallback

router = Router()


# From announcement creation
@router.message(F.photo, AnnouncementCreationStates.UPLOAD_GALLERY)
@router.message(FormCancelFilter(AnnouncementCreationStates))
# From user menu
@router.message(F.text == __("Back"), UserStates.MENU)
# From announcements feed
@router.callback_query(BackCallback.filter(), AnnouncementsStates.FEED)
# From login and register
@router.message(F.text == __("Submit"), RegisterStates.SUBMIT_MENU)
@router.message(F.text, LoginStates.ENTER_PASSWORD)
async def main_menu(
        event: Union[Message, CallbackQuery],
        bot: Bot,
        album_messages: list[Message] | None = None,
        **kwargs
):
    repository: Repository = kwargs.get("repository")

    state: FSMContext = kwargs.get("state")
    current_state = await state.get_state()

    if current_state == RegisterStates.SUBMIT_MENU:
        data = await state.get_data()

        register_data: RegisterScheme = RegisterScheme(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            password=data.get("password")
        )

        async with RequestContext(
                event=event,
                state=state,
                repository=repository
        ) as request:
            await request.register(data=register_data)

    elif current_state == LoginStates.ENTER_PASSWORD:
        if validate_password(event.text):
            await state.update_data({"password": event.text})

            data = await state.get_data()

            login_data: LoginScheme = LoginScheme(
                email=data.get("email"),
                password=data.get("password")
            )

            async with RequestContext(
                    event=event,
                    state=state,
                    repository=repository
            ) as request:
                await request.login(data=login_data)
        else:
            return await event.answer(
                text=_("Validation error. Please, enter password again:"),
                reply_markup=get_login_enter_password_keyboard()
            )

    elif all([
        current_state == AnnouncementCreationStates.UPLOAD_GALLERY,
        isinstance(event, Message) and bool(event.media_group_id)
    ]):
        photo_ids = [m.photo[-1].file_id for m in album_messages]
        await state.update_data({"gallery": photo_ids})

        data = await state.get_data()

        async with RequestContext(
                event=event,
                state=state,
                repository=repository
        ) as request:
            apartment = CreateApartmentSchema(
                address=data.get("address"),
                longitude=float(data.get("longitude")),
                latitude=float(data.get("latitude")),
                district=data.get("district"),
                microdistrict=data.get("microdistrict"),
                technology=data.get("technology"),
                property_type=data.get("property_type"),
                ownership_type=data.get("ownership_type"),
                bedrooms=data.get("bedrooms"),
                bathrooms=data.get("bathrooms"),
                kitchen_area=float(data.get("kitchen_area")),
                heating=data.get("heating"),
                has_balcony_or_loggia=data.get("has_balcony_or_loggia"),
                has_mortgage=data.get("has_mortgage"),
                commission_to_agent=Commission(int(data.get("commission_to_agent"))),
                condition=data.get("condition"),
                finishing=data.get("finishing"),
                rooms=Rooms(int(data.get("rooms"))),
                area=float(data.get("area")),
                call_method=data.get("call_method"),
                description=data.get("description"),
                price=int(data.get("price")),
                scheme=await file_id_to_base64(data.get("scheme"), bot),
                gallery=[
                    Base64Item(
                        action=Action.CREATED,
                        base64=await file_id_to_base64(file_id, bot),
                        order=index
                    ) for (index, file_id) in enumerate(data.get("gallery"))
                ]
            )

        response: SuccessResponse[IDResponseSchema] = await request.create_apartment(apartment)
        await request.create_announcement(data=CreateAnnouncementSchema(
            viewing_time=format_viewing_time(data.get("viewing_time")),
            apartment_id=response["data"]["id"]
        ))

        await event.answer(
            text=_("Announcement was created successfully."),
        )


    await state.clear()
    await state.set_state(MainStates.MAIN_MENU)

    if isinstance(event, CallbackQuery):
        await event.message.delete()

        return await event.message.answer(
            text=_("Select action:"),
            reply_markup=get_main_menu_keyboard()
        )
    else:
        return await event.answer(
            text=_("Select action:"),
            reply_markup=get_main_menu_keyboard()
        )
