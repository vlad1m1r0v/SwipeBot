from aiogram.fsm.state import StatesGroup, State

class AnnouncementsStates(StatesGroup):
    FEED = State()
    GEO = State()
