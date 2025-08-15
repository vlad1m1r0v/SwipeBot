import os
from dotenv import load_dotenv

import asyncio

from aiogram import Dispatcher, Bot
from aiogram.utils.i18n import I18n
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.client.default import DefaultBotProperties

from redis.asyncio import Redis

from bot.utilities.enums import Language
from bot.handlers import register_commands
from bot.utilities.dirs import ENV_PATH, LOCALES_DIR
from bot.database.repository import Repository
from bot.middlewares import CustomI18nMiddleware, AuthMiddleware


async def bot_start() -> None:
    redis = Redis.from_url(os.getenv("REDIS_URI"))
    repository = Repository(mongo_uri=os.getenv("MONGO_URI"))

    dispatcher = Dispatcher(storage=RedisStorage(redis=redis))

    i18n = I18n(path=LOCALES_DIR, default_locale=Language.EN, domain='messages')
    i18n_middleware = CustomI18nMiddleware(i18n)

    i18n_middleware.setup(dispatcher)

    dispatcher.message.middleware(AuthMiddleware())
    dispatcher.callback_query.middleware(AuthMiddleware())

    register_commands(dispatcher)

    bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode='HTML'))

    await dispatcher.start_polling(bot, repository=repository)


def main():
    try:
        if ENV_PATH.exists():
            load_dotenv(ENV_PATH)

        asyncio.run(bot_start())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()
