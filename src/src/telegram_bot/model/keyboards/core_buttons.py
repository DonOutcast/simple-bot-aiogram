from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup



menu_buttons = [
    # [
    #     KeyboardButton(text='Локация', request_location=True),
    # ],
    [KeyboardButton(text="Погода 🌤️"), KeyboardButton(text="Валюта 💰")],
    [KeyboardButton(text="Милота 🐱"), KeyboardButton(text="Опрос 📝")],
    
]

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=menu_buttons, resize_keyboard=True,)
