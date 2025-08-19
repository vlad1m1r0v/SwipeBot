from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    PROFILE = State()
    ANNOUNCEMENTS = State()