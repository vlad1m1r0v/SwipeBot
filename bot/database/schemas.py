from typing import Optional, TypedDict

from dataclasses import dataclass

from bot.utilities.enums import Language


@dataclass
class CreateUser:
    telegram_id: int
    language: Optional[str] = Language.EN

@dataclass
class UpdateUser:
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    language: Optional[str] = None


class GetUser(TypedDict):
    _id: str
    telegram_id: int
    access_token: Optional[str]
    refresh_token: Optional[str]
    language: str


__all__ = ("CreateUser", "UpdateUser", "GetUser")
