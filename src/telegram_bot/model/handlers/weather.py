from aiogram import Router, F
from aiogram.types import Message, Location
from aiogram.fsm.context import FSMContext

from model.template.templates import RenderTemplate

from model.fsm.coordinates import CoordinatesStates
from model.keyboards.core_buttons import generate_keyboard

render = RenderTemplate()

weather_router = Router()
weather_menu_buttons = generate_keyboard(
    [
        [
            "Локация location",
            "Координаты "

        ],
        [
            "Вернуться в главное меню 📜"
        ]

    ],
    request_location=True
)

headers = {"throttling_key": "default", "long_operation": "typing"}


@weather_router.message(F.text == "Погода 🌤️", flags=headers)
async def weather_menu(message: Message):
    await message.answer(
        text=render.render_template("weather.html", {"user_name": message.from_user.first_name}),
        reply_markup=weather_menu_buttons)


@weather_router.message(F.location)
async def location_admin(message: Message, state: FSMContext):
    await state.set_state(CoordinatesStates.longitude)
    await state.update_data(longitude=message.location.longitude)
    await state.set_state(CoordinatesStates.latitude)
    await state.update_data(latitude=message.location.latitude)
    data = await state.get_data()
    await state.clear()

# @admin_router.message(CoordinatesStates.longitude)
# async def longitude_function(message: Message, state: FSMContext):
#     await state.update_data(longitude=message.location.longitude)
#     await state.set_state(CoordinatesStates.latitude)

# @admin_router.message(CoordinatesStates.latitude)
# async def latiude_function(message: Message, state: FSMContext):
#     await state.update_data(latitude=message.location.longitude)
#     data = await state.get_data()
#     print(data.latitude)
#     print(data.longitude)
