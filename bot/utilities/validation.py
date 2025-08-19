import re

UPPERCASE_LETTER = r"[A-Z]"
DIGIT = r"\d"
SPECIAL_CHARACTER = r"[!@#$%^&*()_\-+=,.?\":{}|<>]"
PHONE_NUMBER = r"^\+380\d{9}$"
EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


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


__all__ = (
    "validate_name",
    "validate_email",
    "validate_phone_number",
    "validate_password"
)
