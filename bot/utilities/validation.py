import re

UPPERCASE_LETTER = r"[A-Z]"
DIGIT = r"\d"
SPECIAL_CHARACTER = r"[!@#$%^&*()_\-+=,.?\":{}|<>]"
PHONE_NUMBER = r"^\+380\d{9}$"
EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
TIME = r"^(([01]\d)|(2[0-3])):[0-5]\d$"
FLOAT = r"^\d+(\.\d+)?$"
PRICE = r"^\d{5,7}$"


def validate_name(name: str) -> bool:
    return 3 <= len(name.strip()) <= 100


def validate_email(email: str) -> bool:
    return bool(re.match(EMAIL, email))


def validate_phone_number(number: str) -> bool:
    return bool(re.match(PHONE_NUMBER, number))


def validate_password(password: str) -> bool:
    is_good_length = len(password) >= 8
    has_uppercase_letter = re.search(UPPERCASE_LETTER, password)
    has_digit = re.search(DIGIT, password)
    has_special_character = re.search(SPECIAL_CHARACTER, password)

    return all([
        is_good_length,
        has_uppercase_letter,
        has_digit,
        has_special_character
    ])


def validate_viewing_time(time: str) -> bool:
    return bool(re.match(TIME, time))


def validate_address(address: str) -> bool:
    return 20 < len(address) < 100


def validate_district(address: str) -> bool:
    return 3 < len(address) < 50


def validate_microdistrict(address: str) -> bool:
    return 3 < len(address) < 50


def validate_kitchen_area(kitchen_area: str) -> bool:
    if bool(re.match(FLOAT, kitchen_area)):
        area = float(kitchen_area)
        return area < 1000
    return False


def validate_area(area: str) -> bool:
    if bool(re.match(FLOAT, area)):
        area = float(area)
        return area < 10000
    return False


def validate_description(description: str) -> bool:
    return 20 < len(description) < 1000


def validate_price(price: str) -> bool:
    return bool(re.match(PRICE, price))


__all__ = (
    "validate_name",
    "validate_email",
    "validate_phone_number",
    "validate_password",
    "validate_viewing_time",
    "validate_address",
    "validate_district",
    "validate_microdistrict",
    "validate_kitchen_area",
    "validate_area",
    "validate_description",
    "validate_price"
)
