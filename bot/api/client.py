from dataclasses import asdict

from httpx import AsyncClient, HTTPStatusError

from bot.utilities.pagination import (
    ANNOUNCEMENTS_PER_PAGE,
    MY_ANNOUNCEMENTS_PER_PAGE
)

from bot.database import (
    Repository,
    GetUser,
    UpdateUser
)

from .schemas import (
    LoginScheme,
    RegisterScheme,
    TokensSchema,
    SuccessResponse,
    PaginatedResponse,
    GetAnnouncementSchema,
    GetUserSchema
)


class APIClient:
    def __init__(
            self,
            server_url: str,
            telegram_id: int,
            repository: Repository,
    ):
        self.__client = AsyncClient(base_url=server_url)
        self.__telegram_id = telegram_id
        self.__repository = repository

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__client.aclose()

    async def __make_request(self, method: str, path: str, **kwargs) -> SuccessResponse:
        response = await self.__client.request(method, path, **kwargs)
        response.raise_for_status()
        return response.json()

    async def __make_authorized_request(self, method: str, path: str, **kwargs) -> SuccessResponse:
        user: GetUser = await self.__repository.get_user(self.__telegram_id)
        try:
            response = await self.__client.request(
                method=method,
                url=path,
                headers={"Authorization": f"Bearer {user.get('access_token')}"},
                **kwargs
            )
            response.raise_for_status()
            return response.json()
        except HTTPStatusError as e:
            # Invalid token exception (Token is expired) or token not provided.
            if e.response.status_code in [400, 401]:
                updated_user = await self.__refresh_tokens(
                    refresh_token=user.get("refresh_token")
                )
                response = await self.__client.request(
                    method=method,
                    url=path,
                    headers={"Authorization": f"Bearer {updated_user.get('access_token')}"},
                    **kwargs
                )
                response.raise_for_status()
                return response.json()
            else:
                raise e

    async def __refresh_tokens(self, refresh_token: str) -> GetUser:
        response: SuccessResponse[TokensSchema] = await self.__make_request(
            method="POST",
            path="/auth/tokens/refresh",
            headers={"Authorization": f"Bearer {refresh_token}"}
        )

        tokens = response["data"]

        await self.__repository.update_user(
            telegram_id=self.__telegram_id,
            data=UpdateUser(
                access_token=tokens["access_token"],
                refresh_token=tokens["refresh_token"],
            )
        )

        return await self.__repository.get_user(telegram_id=self.__telegram_id)

    async def login(self, data: LoginScheme) -> SuccessResponse[TokensSchema]:
        response: SuccessResponse[TokensSchema] = await self.__make_authorized_request(
            method="POST",
            path="/auth/user/login",
            json=asdict(data)
        )

        await self.__repository.update_user(
            telegram_id=self.__telegram_id,
            data=UpdateUser(
                access_token=response["data"]["access_token"],
                refresh_token=response["data"]["refresh_token"],
            )
        )

        return response

    async def register(self, data: RegisterScheme) -> SuccessResponse[TokensSchema]:
        response: SuccessResponse[TokensSchema] = await self.__make_authorized_request(
            method="POST",
            path="/auth/user/register",
            json=asdict(data)
        )

        await self.__repository.update_user(
            telegram_id=self.__telegram_id,
            data=UpdateUser(
                access_token=response["data"]["access_token"],
                refresh_token=response["data"]["refresh_token"],
            )
        )

        return response

    async def get_announcements(
            self, offset: int
    ) -> SuccessResponse[PaginatedResponse[GetAnnouncementSchema]]:
        return await self.__make_authorized_request(
            method="GET",
            path="/announcements",
            params={"limit": ANNOUNCEMENTS_PER_PAGE, "offset": offset}
        )

    async def get_my_announcements(
            self, offset: int
    ) -> SuccessResponse[PaginatedResponse[GetAnnouncementSchema]]:
        return await self.__make_authorized_request(
            method="GET",
            path="/user/announcements",
            params={"limit": MY_ANNOUNCEMENTS_PER_PAGE, "offset": offset}
        )

    async def get_profile(self) -> SuccessResponse[GetUserSchema]:
        return await self.__make_authorized_request(
            method="GET",
            path="/user/profile"
        )