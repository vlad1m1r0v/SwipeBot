from .start import get_start_menu_keyboard
from .language import get_language_menu_keyboard
from .auth import (
    get_login_enter_email_keyboard,
    get_login_enter_password_keyboard,
    get_register_enter_name_keyboard,
    get_register_enter_email_keyboard,
    get_register_enter_phone_keyboard,
    get_register_enter_password_keyboard,
    get_register_submit_menu_keyboard,
    get_register_edit_name_keyboard,
    get_register_edit_email_keyboard,
    get_register_edit_phone_keyboard,
    get_register_edit_password_keyboard
)
from .main import get_main_menu_keyboard
from .announcements import (
    get_announcements_feed_inline_keyboard,
    get_geo_inline_keyboard
)
from .profile import (
    get_profile_menu_keyboard,
    get_profile_announcements_keyboard,
    get_profile_information_keyboard
)
from .announcement_creation import (
    get_announcement_creation_enter_viewing_time_keyboard,
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

__all__ = (
    "get_language_menu_keyboard",
    "get_start_menu_keyboard",
    "get_login_enter_email_keyboard",
    "get_login_enter_password_keyboard",
    "get_register_enter_name_keyboard",
    "get_register_enter_email_keyboard",
    "get_register_enter_phone_keyboard",
    "get_register_enter_password_keyboard",
    "get_register_submit_menu_keyboard",
    "get_register_edit_name_keyboard",
    "get_register_edit_email_keyboard",
    "get_register_edit_phone_keyboard",
    "get_register_edit_password_keyboard",
    "get_main_menu_keyboard",
    "get_announcements_feed_inline_keyboard",
    "get_geo_inline_keyboard",
    "get_profile_menu_keyboard",
    "get_profile_announcements_keyboard",
    "get_profile_information_keyboard",
    "get_announcement_creation_enter_viewing_time_keyboard",
    "get_announcement_creation_share_location_keyboard",
    "get_announcement_creation_enter_district_keyboard",
    "get_announcement_creation_enter_microdistrict_keyboard",
    "get_announcement_creation_select_technology_keyboard",
    "get_announcement_creation_select_property_type_keyboard",
    "get_announcement_creation_select_ownership_type_keyboard",
    "get_announcement_creation_select_bedrooms_keyboard",
    "get_announcement_creation_select_bathrooms_keyboard",
    "get_announcement_creation_enter_kitchen_area_keyboard",
    "get_announcement_creation_select_heating_keyboard",
    "get_announcement_creation_select_has_balcony_or_loggia_keyboard",
    "get_announcement_creation_select_has_mortgage_keyboard",
    "get_announcement_creation_select_commission_keyboard",
    "get_announcement_creation_select_apartment_condition_keyboard",
    "get_announcement_creation_select_finishing_keyboard",
    "get_announcement_creation_select_rooms_keyboard",
    "get_announcement_creation_enter_area_keyboard",
    "get_announcement_creation_select_call_method_keyboard",
    "get_announcement_creation_enter_description_keyboard",
    "get_announcement_creation_enter_price_keyboard",
    "get_announcement_creation_upload_scheme_keyboard",
    "get_announcement_creation_upload_gallery_keyboard"
)
