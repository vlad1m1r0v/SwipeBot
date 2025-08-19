from aiogram import Router

from .start import router as start_router
from .language import router as language_router
from .auth import router as auth_router

router = Router()

router.include_routers(
    start_router,
    language_router,
    auth_router
)

__all__ = ("router",)
