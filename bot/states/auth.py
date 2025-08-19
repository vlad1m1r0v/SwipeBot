from aiogram.fsm.state import StatesGroup, State

class RegisterStates(StatesGroup):
    ENTER_NAME = State()
    ENTER_PHONE = State()
    ENTER_EMAIL = State()
    ENTER_PASSWORD = State()
    EDIT_NAME = State()
    EDIT_PHONE = State()
    EDIT_EMAIL = State()
    EDIT_PASSWORD = State()
    SUBMIT_MENU = State()


class LoginStates(StatesGroup):
    ENTER_EMAIL = State()
    ENTER_PASSWORD = State()
