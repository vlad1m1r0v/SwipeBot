from aiogram.filters.callback_data import CallbackData

class PaginationCallback(CallbackData, prefix="page"):
    offset: int