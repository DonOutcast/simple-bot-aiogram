from typing import Optional

from aiogram import Router, F
from aiogram.types import Message, Location
from aiogram.fsm.context import FSMContext
from aiohttp import ClientSession

from model.template.templates import RenderTemplate
from model.fsm.coordinates import CoordinatesStates
from model.keyboards.core_buttons import generate_keyboard
from model.services.crud_openweather import fetch_json
from model.services.weather_help import Coordinates, Weather
from model.services.weather_base import get_weather

render = RenderTemplate()

currency_router = Router()
weather_menu_buttons = generate_keyboard(
    [
        [
            "Курс 💵💶",
            "Конвертировать 🧾"

        ],
        [
            "Вернуться в главное меню 📜"
        ]

    ],
    request_location=True
)

headers = {"throttling_key": "default", "long_operation": "typing"}


@currency_router.message(F.text == "Валюта 💰", flags=headers)
async def currency_menu(message: Message):
    await message.answer(
        text=render.render_template("currency.html", {"user_name": message.from_user.first_name}),
        reply_markup=weather_menu_buttons)


@currency_router.message(F.text == "Курс 💵💶")
async def get_today_currency(message: Message):

    await message.answer(text=render.render_template())


# @weather_router.message(F.location)
# async def location_admin(message: Message, state: FSMContext, aiohttp_session: ClientSession):
#     await state.set_state(CoordinatesStates.longitude)
#     await state.update_data(longitude=message.location.longitude)
#     await state.set_state(CoordinatesStates.latitude)
#     await state.update_data(latitude=message.location.latitude)
#     data: dict = await state.get_data()
#     result: Optional[Weather] = await get_weather_result(data, aiohttp_session)
#     await message.answer(text=render.render_template("format_weather.html", {"weather": result}))
#     await state.clear()
#
#
# @weather_router.message(F.text == "Координаты")
# async def cmd_coordinates(message: Message, state: FSMContext):
#     await state.set_state(CoordinatesStates.latitude)
#     await message.answer(render.render_template("latitude.html"))
#
#
# @weather_router.message(CoordinatesStates.latitude)
# async def latitude_function(message: Message, state: FSMContext):
#     if check_coordinates(message.text):
#         await state.update_data(latitude=message.text)
#         await message.answer(render.render_template("longitude.html"))
#         await state.set_state(CoordinatesStates.longitude)
#     else:
#         await message.delete()
#         await message.answer(render.render_template("latitude.html"))
#         await state.set_state(CoordinatesStates.latitude)
#
#
# @weather_router.message(CoordinatesStates.longitude)
# async def longitude_function(message: Message, state: FSMContext, aiohttp_session: ClientSession):
#     if check_coordinates(message.text):
#         await state.update_data(longitude=message.text)
#         data = await state.get_data()
#         result: Optional[Weather] = await get_weather_result(data, aiohttp_session)
#         await message.answer(text=render.render_template("format_weather.html", {"weather": result}))
#         await state.clear()
#     else:
#         await message.delete()
#         await message.answer(render.render_template("longitude.html"))
#         await state.set_state(CoordinatesStates.longitude)
