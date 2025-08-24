from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _

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


def get_announcement_creation_enter_viewing_time_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter viewing time...")
    )


def get_announcement_creation_share_location_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Share location...")
    )


def get_announcement_creation_enter_district_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter district...")
    )


def get_announcement_creation_enter_microdistrict_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter microdistrict...")
    )


def get_announcement_creation_select_technology_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=technology.value)) for technology in Technology],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select technology...")
    )


def get_announcement_creation_select_property_type_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=property_type.value)) for property_type in PropertyType],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select property type...")
    )


def get_announcement_creation_select_ownership_type_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=ownership_type.value)) for ownership_type in OwnershipType],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select ownership type...")
    )


def get_announcement_creation_select_bedrooms_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=bedrooms.value)) for bedrooms in Bedrooms],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select bedrooms...")
    )


def get_announcement_creation_select_bathrooms_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=bathrooms.value)) for bathrooms in Bathrooms],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select bathrooms...")
    )


def get_announcement_creation_enter_kitchen_area_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter kitchen area...")
    )


def get_announcement_creation_select_heating_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=heating.value)) for heating in Heating],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select heating...")
    )


def get_announcement_creation_select_has_balcony_or_loggia_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Yes")), KeyboardButton(text=_("No"))],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select option...")
    )


def get_announcement_creation_select_has_mortgage_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Yes")), KeyboardButton(text=_("No"))],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select option...")
    )


def get_announcement_creation_select_commission_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=str(commission.value))) for commission in Commission],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select commission...")
    )


def get_announcement_creation_select_apartment_condition_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=condition.value)) for condition in ApartmentCondition],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select apartment condition...")
    )


def get_announcement_creation_select_finishing_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=finishing.value)) for finishing in Finishing],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select finishing...")
    )


def get_announcement_creation_select_rooms_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=str(rooms.value))) for rooms in Rooms],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select rooms...")
    )


def get_announcement_creation_enter_area_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter area...")
    )


def get_announcement_creation_select_call_method_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            *[list(KeyboardButton(text=call_method.value)) for call_method in CallMethod],
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Select call method...")
    )


def get_announcement_creation_enter_description_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter description...")
    )


def get_announcement_creation_enter_price_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter price...")
    )


def get_announcement_creation_upload_scheme_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Upload scheme...")
    )


def get_announcement_creation_upload_gallery_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Upload gallery...")
    )
