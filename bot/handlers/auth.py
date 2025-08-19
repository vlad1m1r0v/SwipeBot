from typing import TypedDict, Callable

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.fsm.state import State
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.states import (StartStates, RegisterStates, LoginStates)
from bot.keyboards import (
    get_register_enter_name_keyboard,
    get_register_enter_email_keyboard,
    get_register_enter_phone_keyboard,
    get_register_enter_password_keyboard,
    get_register_submit_menu_keyboard,
    get_register_edit_name_keyboard,
    get_register_edit_email_keyboard,
    get_register_edit_phone_keyboard,
    get_register_edit_password_keyboard,
    get_login_enter_password_keyboard,
    get_login_enter_email_keyboard,

)
from bot.utilities.validation import (
    validate_name,
    validate_email,
    validate_phone_number,
    validate_password
)

router = Router()


@router.message(F.text == __("Back"), RegisterStates.ENTER_EMAIL)
@router.message(F.text == __("Register"), StartStates.START_MENU)
async def register_enter_name(message: Message, state: FSMContext):
    await state.set_state(RegisterStates.ENTER_NAME)
    await message.answer(
        text=_("Enter name:"),
        reply_markup=get_register_enter_name_keyboard()
    )


@router.message(F.text == __("Back"), RegisterStates.ENTER_PHONE)
@router.message(F.text, RegisterStates.ENTER_NAME)
async def register_enter_email(message: Message, state: FSMContext):
    name = message.text
    if validate_name(name):
        await state.update_data({"name": name})
        await state.set_state(RegisterStates.ENTER_EMAIL)
        await message.answer(
            text=_("Enter email:"),
            reply_markup=get_register_enter_email_keyboard()
        )
    else:
        await state.set_state(RegisterStates.ENTER_NAME)
        await message.answer(
            text=_("Validation error. Please, enter name again:"),
            reply_markup=get_register_enter_name_keyboard()
        )


@router.message(F.text == __("Back"), RegisterStates.ENTER_PASSWORD)
@router.message(F.text, RegisterStates.ENTER_EMAIL)
async def register_enter_phone(message: Message, state: FSMContext):
    email = message.text
    if validate_email(email):
        await state.update_data({"email": email})
        await state.set_state(RegisterStates.ENTER_PHONE)
        await message.answer(
            text=_("Enter phone:"),
            reply_markup=get_register_enter_phone_keyboard()
        )
    else:
        await state.set_state(RegisterStates.ENTER_EMAIL)
        await message.answer(
            text=_("Validation error. Please, enter email again:"),
            reply_markup=get_register_enter_email_keyboard()
        )


@router.message(F.text, RegisterStates.ENTER_PHONE)
async def register_enter_password(message: Message, state: FSMContext):
    phone = message.text
    if validate_phone_number(phone):
        await state.update_data({"phone": phone})
        await state.set_state(RegisterStates.ENTER_PASSWORD)
        await message.answer(
            text=_("Enter password:"),
            reply_markup=get_register_enter_password_keyboard()
        )
    else:
        await state.set_state(RegisterStates.ENTER_PHONE)
        await message.answer(
            text=_("Validation error. Please, enter phone again:"),
            reply_markup=get_register_enter_phone_keyboard()
        )


@router.message(F.text == __("Back"), RegisterStates.EDIT_NAME)
@router.message(F.text == __("Back"), RegisterStates.EDIT_EMAIL)
@router.message(F.text == __("Back"), RegisterStates.EDIT_PHONE)
@router.message(F.text == __("Back"), RegisterStates.EDIT_PASSWORD)
@router.message(F.text, RegisterStates.EDIT_NAME)
@router.message(F.text, RegisterStates.EDIT_EMAIL)
@router.message(F.text, RegisterStates.EDIT_PHONE)
@router.message(F.text, RegisterStates.EDIT_PASSWORD)
@router.message(F.text, RegisterStates.ENTER_PASSWORD)
async def register_submit_menu(message: Message, state: FSMContext):
    async def render_submit_menu() -> None:
        data = await state.get_data()
        await state.set_state(RegisterStates.SUBMIT_MENU)

        text = (f"{_('Entered name:')} {data.get('name')}\n" +
                f"{_('Entered email:')} {data.get('email')}\n" +
                f"{_('Entered phone:')} {data.get('phone')}\n" +
                f"{_('Entered password:')} {data.get('password')}\n" +
                f"{_('Select action:')}")

        await message.answer(
            text=text,
            reply_markup=get_register_submit_menu_keyboard()
        )

    class Case(TypedDict):
        field: str
        validation_rule: Callable[[str], bool]
        state: State
        keyboard: ReplyKeyboardMarkup

    cases: list[Case] = [
        Case(
            state=RegisterStates.ENTER_PASSWORD,
            field="password",
            validation_rule=validate_password,
            keyboard=get_register_enter_password_keyboard(),
        ),
        Case(
            state=RegisterStates.EDIT_NAME,
            field="name",
            validation_rule=validate_name,
            keyboard=get_register_edit_name_keyboard(),
        ),
        Case(
            state=RegisterStates.EDIT_EMAIL,
            field="email",
            validation_rule=validate_email,
            keyboard=get_register_edit_email_keyboard(),
        ),
        Case(
            state=RegisterStates.EDIT_PHONE,
            field="phone",
            validation_rule=validate_phone_number,
            keyboard=get_register_edit_phone_keyboard(),
        ),
        Case(
            state=RegisterStates.EDIT_PASSWORD,
            field="password",
            validation_rule=validate_password,
            keyboard=get_register_edit_password_keyboard(),
        ),
    ]

    value = message.text

    if value == _("Back"):
        await render_submit_menu()
    else:
        current_state = await state.get_state()
        for state_case in cases:
            if state_case.get("state") == current_state:
                if state_case.get("validation_rule")(value):
                    await state.update_data({state_case.get("field"): value})
                    await state.set_state(RegisterStates.SUBMIT_MENU)
                    await render_submit_menu()
                else:
                    await state.set_state(state_case.get("state"))
                    await message.answer(
                        text=_("Validation error. Please, enter {} again:").format(state_case.get("field")),
                        reply_markup=state_case.get("keyboard")
                    )


@router.message(F.text == __("Edit name"), RegisterStates.SUBMIT_MENU)
async def register_edit_name(message: Message, state: FSMContext):
    await state.set_state(RegisterStates.EDIT_NAME)
    await message.answer(
        text=_("Enter name:"),
        reply_markup=get_register_edit_name_keyboard()
    )


@router.message(F.text == __("Edit email"), RegisterStates.SUBMIT_MENU)
async def register_edit_email(message: Message, state: FSMContext):
    await state.set_state(RegisterStates.EDIT_EMAIL)
    await message.answer(
        text=_("Enter email:"),
        reply_markup=get_register_edit_email_keyboard()
    )


@router.message(F.text == __("Edit phone"), RegisterStates.SUBMIT_MENU)
async def register_edit_phone(message: Message, state: FSMContext):
    await state.set_state(RegisterStates.EDIT_PHONE)
    await message.answer(
        text=_("Enter phone:"),
        reply_markup=get_register_edit_phone_keyboard()
    )


@router.message(F.text == __("Edit password"), RegisterStates.SUBMIT_MENU)
async def register_edit_password(message: Message, state: FSMContext):
    await state.set_state(RegisterStates.EDIT_PASSWORD)
    await message.answer(
        text=_("Enter password:"),
        reply_markup=get_register_edit_password_keyboard()
    )
