from aiogram.types import BotCommand


def get_commands() -> list[BotCommand]:
    commands: list[BotCommand] = [
        BotCommand(
            command="start",
            description=
            "Begin work with bot. Greets with message and returns reply keyboard with options 'Login' / 'Register' / 'Change language'."
        )
    ]

    return commands
