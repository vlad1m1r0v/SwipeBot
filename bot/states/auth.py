from aiogram.fsm.state import StatesGroup, State

class AuthStates(StatesGroup):
    START = State()

class RegisterStates(StatesGroup):
    ENTER_NAME = State()
    ENTER_PHONE = State()
    ENTER_EMAIL = State()
    ENTER_PASSWORD = State()
    EDIT_NAME = State()
    EDIT_PHONE = State()
    EDIT_EMAIL = State()
    EDIT_PASSWORD = State()
    SUBMIT_FORM = State()


class LoginStates(StatesGroup):
    ENTER_EMAIL = State()
    ENTER_PASSWORD = State()
