from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from model.template.templates import render
from model.keyboards.core_buttons import generate_keyboard

menu_keyboard = generate_keyboard(
    [
        [
            "Погода 🌤️",
            "Валюта 💰"
        ],
        [
            "Милота 🐱",
            "Опрос 📝"
        ],

    ],
)


back_to_menu_router = Router()
headers = {"throttling_key": "default", "long_operation": "typing"}


@back_to_menu_router.message(F.text == "Вернуться в главное меню 📜", flags=headers)
async def cmd_cancel_registration(message: types.Message, state: FSMContext):
    await message.delete()
    try:
        await message.delete(message_id=message.message_id - 1)
    except:
        pass
    current_state = await state.get_state()
    if current_state is None:
        await message.answer('Вы вернулись в главное меню', reply_markup=menu_keyboard)
        await message.answer_sticker(sticker="CAACAgIAAxkBAAENm1Bi_0Q9YClvUdjgvDLx0S5V3Z3UUgAClgcAAmMr4glEcXCvl0uDLSkE")
        return
    await state.clear()
    await message.answer('Вы вернулись в главное меню', reply_markup=menu_keyboard)
    await message.answer_sticker(sticker="CAACAgIAAxkBAAENm1Bi_0Q9YClvUdjgvDLx0S5V3Z3UUgAClgcAAmMr4glEcXCvl0uDLSkE")