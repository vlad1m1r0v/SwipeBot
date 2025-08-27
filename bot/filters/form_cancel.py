from typing import Type
from aiogram.types import Message
from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup
from aiogram.utils.i18n import gettext as _

class FormCancelFilter(BaseFilter):
    def __init__(self, states_group: Type[StatesGroup]):
        self.states_group = states_group
        self.first_state = list(states_group.__states__)[0]

    async def __call__(self, message: Message, state: FSMContext) -> bool:
        current_state_name = await state.get_state()
        if not current_state_name:
            return False

        current_group_name = current_state_name.split(':')[0]

        is_in_group = current_group_name == self.states_group.__name__

        is_cancel = message.text == _("Cancel")
        is_back = message.text == _("Back")

        is_at_first_state = current_state_name == self.first_state.state
        is_back_at_first_state = is_back and is_at_first_state

        return is_in_group and (is_cancel or is_back_at_first_state)