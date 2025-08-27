from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.states import (MainStates, AnnouncementCreationStates)
from bot.api import (
    Technology,
    PropertyType,
    OwnershipType,
    Bedrooms,
    Bathrooms,
    Heating,
    Commission,
    ApartmentCondition,
    Finishing,
    Rooms,
    CallMethod
)
from bot.keyboards import (
    get_announcement_creation_enter_viewing_time_keyboard,
    get_announcement_creation_enter_address_keyboard,
    get_announcement_creation_share_location_keyboard,
    get_announcement_creation_enter_district_keyboard,
    get_announcement_creation_enter_microdistrict_keyboard,
    get_announcement_creation_select_technology_keyboard,
    get_announcement_creation_select_property_type_keyboard,
    get_announcement_creation_select_ownership_type_keyboard,
    get_announcement_creation_select_bedrooms_keyboard,
    get_announcement_creation_select_bathrooms_keyboard,
    get_announcement_creation_enter_kitchen_area_keyboard,
    get_announcement_creation_select_heating_keyboard,
    get_announcement_creation_select_has_balcony_or_loggia_keyboard,
    get_announcement_creation_select_has_mortgage_keyboard,
    get_announcement_creation_select_commission_keyboard,
    get_announcement_creation_select_apartment_condition_keyboard,
    get_announcement_creation_select_finishing_keyboard,
    get_announcement_creation_select_rooms_keyboard,
    get_announcement_creation_enter_area_keyboard,
    get_announcement_creation_select_call_method_keyboard,
    get_announcement_creation_enter_description_keyboard,
    get_announcement_creation_enter_price_keyboard,
    get_announcement_creation_upload_scheme_keyboard,
    get_announcement_creation_upload_gallery_keyboard
)
from bot.utilities.validation import (
    validate_viewing_time,
    validate_address,
    validate_district,
    validate_microdistrict,
    validate_kitchen_area,
    validate_area,
    validate_description,
    validate_price
)

router = Router()


@router.message(F.text == __("Back"), AnnouncementCreationStates.ENTER_ADDRESS)
@router.message(F.text == __("Create announcement"), MainStates.MAIN_MENU)
async def announcement_creation_enter_viewing_time(message: Message, state: FSMContext):
    await state.set_state(AnnouncementCreationStates.ENTER_VIEWING_TIME)

    await message.answer(
        text=_("Enter viewing time:"),
        reply_markup=get_announcement_creation_enter_viewing_time_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.ENTER_DISTRICT)
@router.message(F.text, AnnouncementCreationStates.ENTER_VIEWING_TIME)
async def announcement_creation_enter_address(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.ENTER_VIEWING_TIME:
        viewing_time = message.text
        if validate_viewing_time(viewing_time):
            await state.update_data({"viewing_time": viewing_time})
        else:
            await state.set_state(AnnouncementCreationStates.ENTER_VIEWING_TIME)
            return await message.answer(
                text=_("Validation error. Please, enter viewing time again:"),
                reply_markup=get_announcement_creation_enter_viewing_time_keyboard()
            )
    await state.set_state(AnnouncementCreationStates.ENTER_ADDRESS)
    return await message.answer(
        text=_("Enter address:"),
        reply_markup=get_announcement_creation_enter_address_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.ENTER_MICRODISTRICT)
@router.message(F.text, AnnouncementCreationStates.ENTER_ADDRESS)
async def announcement_creation_enter_district(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.ENTER_ADDRESS:
        address = message.text
        if validate_address(address):
            await state.update_data({"address": address})
        else:
            await state.set_state(AnnouncementCreationStates.ENTER_ADDRESS)
            return await message.answer(
                text=_("Validation error. Please, enter address again:"),
                reply_markup=get_announcement_creation_enter_address_keyboard()
            )
    await state.set_state(AnnouncementCreationStates.ENTER_DISTRICT)
    return await message.answer(
        text=_("Enter district:"),
        reply_markup=get_announcement_creation_enter_district_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SHARE_LOCATION)
@router.message(F.text, AnnouncementCreationStates.ENTER_DISTRICT)
async def announcement_creation_enter_microdistrict(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.ENTER_DISTRICT:
        district = message.text
        if validate_district(district):
            await state.update_data({"district": district})
        else:
            await state.set_state(AnnouncementCreationStates.ENTER_DISTRICT)
            return await message.answer(
                text=_("Validation error. Please, enter district again:"),
                reply_markup=get_announcement_creation_enter_district_keyboard()
            )
    await state.set_state(AnnouncementCreationStates.ENTER_MICRODISTRICT)
    return await message.answer(
        text=_("Enter microdistrict:"),
        reply_markup=get_announcement_creation_enter_microdistrict_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_TECHNOLOGY)
@router.message(F.text, AnnouncementCreationStates.ENTER_MICRODISTRICT)
async def announcement_creation_share_geolocation(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.ENTER_MICRODISTRICT:
        microdistrict = message.text
        if validate_microdistrict(microdistrict):
            await state.update_data({"microdistrict": microdistrict})
        else:
            await state.set_state(AnnouncementCreationStates.ENTER_MICRODISTRICT)
            return await message.answer(
                text=_("Validation error. Please, enter microdistrict again:"),
                reply_markup=get_announcement_creation_enter_viewing_time_keyboard()
            )
    await state.set_state(AnnouncementCreationStates.SHARE_LOCATION)
    return await message.answer(
        text=_("Share geolocation:"),
        reply_markup=get_announcement_creation_share_location_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_OWNERSHIP_TYPE)
@router.message(F.location, AnnouncementCreationStates.SHARE_LOCATION)
async def announcement_creation_select_technology_type(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SHARE_LOCATION:
        latitude = message.location.latitude
        longitude = message.location.longitude
        await state.update_data({"latitude": latitude, "longitude": longitude})

    await state.set_state(AnnouncementCreationStates.SELECT_TECHNOLOGY)
    return await message.answer(
        text=_("Select technology:"),
        reply_markup=get_announcement_creation_select_technology_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_PROPERTY_TYPE)
@router.message(F.text.in_([t.value for t in Technology]), AnnouncementCreationStates.SELECT_TECHNOLOGY)
async def announcement_creation_select_ownership_type(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_TECHNOLOGY:
        await state.update_data({"technology": message.text})

    await state.set_state(AnnouncementCreationStates.SELECT_OWNERSHIP_TYPE)
    return await message.answer(
        text=_("Select ownership type:"),
        reply_markup=get_announcement_creation_select_ownership_type_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_BEDROOMS)
@router.message(F.text.in_([ot.value for ot in OwnershipType]), AnnouncementCreationStates.SELECT_OWNERSHIP_TYPE)
async def announcement_creation_select_property_type(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_OWNERSHIP_TYPE:
        await state.update_data({"ownership_type": message.text})

    await state.set_state(AnnouncementCreationStates.SELECT_PROPERTY_TYPE)
    return await message.answer(
        text=_("Select property type:"),
        reply_markup=get_announcement_creation_select_property_type_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_BATHROOMS)
@router.message(F.text.in_([pt.value for pt in PropertyType]), AnnouncementCreationStates.SELECT_PROPERTY_TYPE)
async def announcement_creation_select_bedrooms(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_PROPERTY_TYPE:
        await state.update_data({"property_type": message.text})

    await state.set_state(AnnouncementCreationStates.SELECT_BEDROOMS)
    return await message.answer(
        text=_("Select bedrooms:"),
        reply_markup=get_announcement_creation_select_bedrooms_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.ENTER_KITCHEN_AREA)
@router.message(F.text.in_([b.value for b in Bedrooms]), AnnouncementCreationStates.SELECT_BEDROOMS)
async def announcement_creation_select_bathrooms(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_BEDROOMS:
        await state.update_data({"bedrooms": message.text})

    await state.set_state(AnnouncementCreationStates.SELECT_BATHROOMS)
    return await message.answer(
        text=_("Select bathrooms:"),
        reply_markup=get_announcement_creation_select_bathrooms_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_HEATING)
@router.message(F.text.in_([b.value for b in Bathrooms]), AnnouncementCreationStates.SELECT_BATHROOMS)
async def announcement_creation_enter_kitchen_area(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_BATHROOMS:
        await state.update_data({"bathrooms": message.text})

    await state.set_state(AnnouncementCreationStates.ENTER_KITCHEN_AREA)
    return await message.answer(
        text=_("Enter kitchen area:"),
        reply_markup=get_announcement_creation_enter_kitchen_area_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_HAS_BALCONY_OR_LOGGIA)
@router.message(F.text, AnnouncementCreationStates.ENTER_KITCHEN_AREA)
async def announcement_creation_select_heating(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.ENTER_KITCHEN_AREA:
        kitchen_area = message.text
        if validate_kitchen_area(kitchen_area):
            await state.update_data({"kitchen_area": kitchen_area})
        else:
            await state.set_state(AnnouncementCreationStates.ENTER_KITCHEN_AREA)
            return await message.answer(
                text=_("Validation error. Please, enter kitchen area again:"),
                reply_markup=get_announcement_creation_enter_kitchen_area_keyboard()
            )

    await state.set_state(AnnouncementCreationStates.SELECT_HEATING)
    return await message.answer(
        text=_("Select heating:"),
        reply_markup=get_announcement_creation_select_heating_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_HAS_MORTGAGE)
@router.message(F.text.in_([h.value for h in Heating]), AnnouncementCreationStates.SELECT_HEATING)
async def announcement_creation_has_balcony_or_loggia(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_HEATING:
        await state.update_data({"heating": message.text})

    await state.set_state(AnnouncementCreationStates.SELECT_HAS_BALCONY_OR_LOGGIA)
    return await message.answer(
        text=_("Select has balcony or loggia:"),
        reply_markup=get_announcement_creation_select_has_balcony_or_loggia_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_COMMISSION_TO_AGENT)
@router.message(F.text.in_([__("Yes"), __("No")]), AnnouncementCreationStates.SELECT_HAS_BALCONY_OR_LOGGIA)
async def announcement_creation_has_mortgage(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_HAS_BALCONY_OR_LOGGIA:
        await state.update_data({"has_balcony_or_loggia": message.text == _("Yes")})

    await state.set_state(AnnouncementCreationStates.SELECT_HAS_MORTGAGE)
    return await message.answer(
        text=_("Select has mortgage:"),
        reply_markup=get_announcement_creation_select_has_mortgage_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_CONDITION)
@router.message(F.text.in_([__("Yes"), __("No")]), AnnouncementCreationStates.SELECT_HAS_MORTGAGE)
async def announcement_creation_select_commission(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_HAS_MORTGAGE:
        await state.update_data({"has_mortgage": message.text == _("Yes")})

    await state.set_state(AnnouncementCreationStates.SELECT_COMMISSION_TO_AGENT)
    return await message.answer(
        text=_("Select commission to agent:"),
        reply_markup=get_announcement_creation_select_commission_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_FINISHING)
@router.message(F.text.in_([str(c.value) for c in Commission]), AnnouncementCreationStates.SELECT_COMMISSION_TO_AGENT)
async def announcement_creation_select_condition(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_COMMISSION_TO_AGENT:
        await state.update_data({"commission_to_agent": message.text})

    await state.set_state(AnnouncementCreationStates.SELECT_CONDITION)
    return await message.answer(
        text=_("Select condition:"),
        reply_markup=get_announcement_creation_select_apartment_condition_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_ROOMS)
@router.message(F.text.in_([ac.value for ac in ApartmentCondition]), AnnouncementCreationStates.SELECT_CONDITION)
async def announcement_creation_select_finishing(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_CONDITION:
        await state.update_data({"condition": message.text})

    await state.set_state(AnnouncementCreationStates.SELECT_FINISHING)
    return await message.answer(
        text=_("Select finishing:"),
        reply_markup=get_announcement_creation_select_finishing_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.ENTER_AREA)
@router.message(F.text.in_([f.value for f in Finishing]), AnnouncementCreationStates.SELECT_FINISHING)
async def announcement_creation_select_rooms(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_FINISHING:
        await state.update_data({"finishing": message.text})

    await state.set_state(AnnouncementCreationStates.SELECT_ROOMS)
    return await message.answer(
        text=_("Select rooms:"),
        reply_markup=get_announcement_creation_select_rooms_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.SELECT_CALL_METHOD)
@router.message(F.text.in_([str(r.value) for r in Rooms]), AnnouncementCreationStates.SELECT_ROOMS)
async def announcement_creation_enter_area(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_ROOMS:
        await state.update_data({"rooms": message.text})

    await state.set_state(AnnouncementCreationStates.ENTER_AREA)
    return await message.answer(
        text=_("Enter area:"),
        reply_markup=get_announcement_creation_enter_area_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.ENTER_DESCRIPTION)
@router.message(F.text, AnnouncementCreationStates.ENTER_AREA)
async def announcement_creation_select_call_method(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.ENTER_AREA:
        area = message.text
        if validate_area(area):
            await state.update_data({"area": area})
        else:
            await state.set_state(AnnouncementCreationStates.ENTER_AREA)
            return await message.answer(
                text=_("Validation error. Please, enter area again:"),
                reply_markup=get_announcement_creation_enter_area_keyboard()
            )

    await state.set_state(AnnouncementCreationStates.SELECT_CALL_METHOD)
    return await message.answer(
        text=_("Select call method:"),
        reply_markup=get_announcement_creation_select_call_method_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.ENTER_PRICE)
@router.message(F.text.in_([cm.value for cm in CallMethod]), AnnouncementCreationStates.SELECT_CALL_METHOD)
async def announcement_creation_enter_description(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.SELECT_CALL_METHOD:
        await state.update_data({"call_method": message.text})

    await state.set_state(AnnouncementCreationStates.ENTER_DESCRIPTION)
    return await message.answer(
        text=_("Enter description:"),
        reply_markup=get_announcement_creation_enter_description_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.UPLOAD_SCHEME)
@router.message(F.text, AnnouncementCreationStates.ENTER_DESCRIPTION)
async def announcement_creation_enter_price(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.ENTER_DESCRIPTION:
        description = message.text
        if validate_description(description):
            await state.update_data({"description": description})
        else:
            await state.set_state(AnnouncementCreationStates.ENTER_DESCRIPTION)
            return await message.answer(
                text=_("Validation error. Please, enter description again:"),
                reply_markup=get_announcement_creation_enter_description_keyboard()
            )

    await state.set_state(AnnouncementCreationStates.ENTER_PRICE)
    return await message.answer(
        text=_("Enter price:"),
        reply_markup=get_announcement_creation_enter_price_keyboard()
    )


@router.message(F.text == __("Back"), AnnouncementCreationStates.UPLOAD_GALLERY)
@router.message(F.text, AnnouncementCreationStates.ENTER_PRICE)
async def announcement_creation_upload_scheme(message: Message, state: FSMContext):
    if await state.get_state() == AnnouncementCreationStates.ENTER_PRICE:
        price = message.text
        if validate_price(price):
            await state.update_data({"price": price})
        else:
            await state.set_state(AnnouncementCreationStates.ENTER_PRICE)
            return await message.answer(
                text=_("Validation error. Please, enter price again:"),
                reply_markup=get_announcement_creation_enter_price_keyboard()
            )

    await state.set_state(AnnouncementCreationStates.UPLOAD_SCHEME)
    return await message.answer(
        text=_("Upload scheme:"),
        reply_markup=get_announcement_creation_upload_scheme_keyboard()
    )


@router.message(F.photo, AnnouncementCreationStates.UPLOAD_SCHEME)
async def announcement_creation_upload_gallery(message: Message, state: FSMContext):
    scheme_id = message.photo[-1].file_id
    await state.update_data({"scheme": scheme_id})
    await state.set_state(AnnouncementCreationStates.UPLOAD_GALLERY)

    return await message.answer(
        text=_("Upload gallery:"),
        reply_markup=get_announcement_creation_upload_gallery_keyboard()
    )
