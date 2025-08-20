from typing import Generic, TypeVar, TypedDict

from datetime import time

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
    floor_no: int
    total_floors: int
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

__all__ = (
    "LoginScheme",
    "RegisterScheme",
    "ErrorResponse",
    "SuccessResponse",
    "PaginatedResponse",
    "TokensSchema",
    "GetAnnouncementSchema"

)
