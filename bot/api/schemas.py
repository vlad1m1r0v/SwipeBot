import enum

from typing import Generic, TypeVar, TypedDict

from datetime import time, datetime

from dataclasses import dataclass

T = TypeVar('T')


class SuccessResponse(TypedDict, Generic[T]):
    data: T


class PaginatedResponse(TypedDict, Generic[T]):
    limit: int
    offset: int
    total: int
    items: list[T]


class ErrorDetail(TypedDict):
    field: str
    message: str


class Error(TypedDict):
    code: str
    details: ErrorDetail


class ErrorResponse(TypedDict):
    status: int
    error: Error


@dataclass
class RegisterScheme:
    name: str
    email: str
    phone: str
    password: str


@dataclass
class LoginScheme:
    email: str
    password: str


class TokensSchema(TypedDict):
    access_token: str
    refresh_token: str


class GetApartmentSchema(TypedDict):
    id: int
    price: int
    rooms: int
    area: float
    floor_no: int | None
    total_floors: int | None
    address: str
    longitude: float
    latitude: float
    preview_url: str


class GetPromotionSchema(TypedDict):
    id: int
    highlight_colour: str
    phrase: str


class GetAnnouncementSchema(TypedDict):
    id: int
    viewing_time: time
    apartment: GetApartmentSchema
    promotion: GetPromotionSchema


class GetContactSchema(TypedDict):
    id: int
    first_name: str | None
    last_name: str | None
    email: str | None
    phone: str | None


class GetBalanceSchema(TypedDict):
    id: int
    value: int


class GetSubscriptionSchema(TypedDict):
    id: int
    is_auto_renewal: bool
    expiry_date: str


class NotificationType(str, enum.Enum):
    DISABLED = "disabled"
    ME = "me"
    AGENT = "agent"
    ME_AND_AGENT = "me_and_agent"


class GetNotificationSettingsSchema(TypedDict):
    id: int
    redirect_notifications_to_agent: bool
    notification_type: NotificationType


class GetUserSchema(TypedDict):
    id: int
    name: str
    email: str
    phone: str
    photo_url: str | None
    contact: GetContactSchema
    agent_contact: GetContactSchema
    balance: GetBalanceSchema
    subscription: GetSubscriptionSchema
    notification_settings: GetNotificationSettingsSchema


__all__ = (
    "LoginScheme",
    "RegisterScheme",
    "ErrorResponse",
    "SuccessResponse",
    "PaginatedResponse",
    "TokensSchema",
    "GetAnnouncementSchema",
    "GetApartmentSchema",
    "GetUserSchema"
)
