from aiogram.filters.callback_data import CallbackData


class GeolocationCallback(CallbackData, prefix="geo"):
    longitude: float
    latitude: float