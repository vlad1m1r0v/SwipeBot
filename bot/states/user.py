from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    MENU = State()
    PROFILE = State()
    ANNOUNCEMENTS = State()