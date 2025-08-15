from aiogram import Router, F
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.filters.command import CommandStart

from bot.states.language import LanguageStates
from bot.handlers.auth import start_menu
from bot.handlers.language import language_menu, set_language, back_to_start


def register_commands(router: Router) -> None:
    router.message.register(start_menu, CommandStart())

    router.message.register(language_menu, F.text == __("Change language"))
    router.message.register(set_language, F.text.in_({"English", "Українська"}), LanguageStates.SWITCH_LANGUAGE)
    router.message.register(back_to_start, F.text == __("Back"), LanguageStates.SWITCH_LANGUAGE)
