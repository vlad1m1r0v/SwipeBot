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

def get_announcement_creation_enter_address_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=_("Enter address...")
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
    technology_rows = [[KeyboardButton(text=technology.value)] for technology in Technology]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=technology_rows + [navigation_row],
        resize_keyboard=True,
        input_field_placeholder=_("Select technology...")
    )


def get_announcement_creation_select_property_type_keyboard() -> ReplyKeyboardMarkup:
    property_type_rows = [[KeyboardButton(text=property_type.value)] for property_type in PropertyType]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=property_type_rows + [navigation_row],
        resize_keyboard=True,
        input_field_placeholder=_("Select property type...")
    )


def get_announcement_creation_select_ownership_type_keyboard() -> ReplyKeyboardMarkup:
    ownership_type_rows = [[KeyboardButton(text=ownership_type.value)] for ownership_type in OwnershipType]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=ownership_type_rows + [navigation_row],
        resize_keyboard=True,
        input_field_placeholder=_("Select ownership type...")
    )


def get_announcement_creation_select_bedrooms_keyboard() -> ReplyKeyboardMarkup:
    bedrooms_rows = [[KeyboardButton(text=bedrooms.value)] for bedrooms in Bedrooms]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=bedrooms_rows + [navigation_row],
        resize_keyboard=True,
        input_field_placeholder=_("Select bedrooms...")
    )


def get_announcement_creation_select_bathrooms_keyboard() -> ReplyKeyboardMarkup:
    bathrooms_rows = [[KeyboardButton(text=bathrooms.value)] for bathrooms in Bathrooms]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=bathrooms_rows + [navigation_row],
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
    heating_rows = [[KeyboardButton(text=heating.value)] for heating in Heating]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=heating_rows + [navigation_row],
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
    commission_rows = [[KeyboardButton(text=str(commission.value))] for commission in Commission]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=commission_rows + [navigation_row],
        resize_keyboard=True,
        input_field_placeholder=_("Select commission...")
    )


def get_announcement_creation_select_apartment_condition_keyboard() -> ReplyKeyboardMarkup:
    condition_rows = [[KeyboardButton(text=condition.value)] for condition in ApartmentCondition]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=condition_rows + [navigation_row],
        resize_keyboard=True,
        input_field_placeholder=_("Select apartment condition...")
    )


def get_announcement_creation_select_finishing_keyboard() -> ReplyKeyboardMarkup:
    finishing_rows = [[KeyboardButton(text=finishing.value)] for finishing in Finishing]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=finishing_rows + [navigation_row],
        resize_keyboard=True,
        input_field_placeholder=_("Select finishing...")
    )


def get_announcement_creation_select_rooms_keyboard() -> ReplyKeyboardMarkup:
    rooms_rows = [[KeyboardButton(text=str(rooms.value))] for rooms in Rooms]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=rooms_rows + [navigation_row],
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
    call_method_rows = [[KeyboardButton(text=call_method.value)] for call_method in CallMethod]
    navigation_row = [KeyboardButton(text=_("Cancel")), KeyboardButton(text=_("Back"))]
    return ReplyKeyboardMarkup(
        keyboard=call_method_rows + [navigation_row],
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
