from typing import Generic, TypeVar, TypedDict

from dataclasses import dataclass

T = TypeVar('T')


class SuccessResponse(TypedDict, Generic[T]):
    data: T


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

__all__ = (
    "LoginScheme",
    "RegisterScheme",
    "ErrorResponse",
    "SuccessResponse",
    "TokensSchema"
)
