from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup

from bs4 import BeautifulSoup
from aiohttp import ClientSession
from datetime import datetime

from model.template.templates import RenderTemplate
from model.keyboards.core_buttons import generate_keyboard
from model.services.crud_currency import fetch_xml
from model.services.currency_base import get_all_currency, get_course
from model.keyboards.currency_buttons import get_currency_markup
from model.call_back_data.call_back_data_currency import ChangePage, CourseCurrency
from model.fsm.currency import CurrencyStates

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
async def get_today_currency(message: Message, aiohttp_session: ClientSession):
    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    url += "date_req?=" + str(today)
    res = await fetch_xml(aiohttp_session, url)
    res_1 = get_all_currency(res)
    # await message.answer(text="s", reply_markup=get_currency_keyboard(0, "all_currency_", res_1))


@currency_router.message(F.text == "Конвертировать 🧾")
async def cmd_convector_currency(message: Message, aiohttp_session: ClientSession, state: FSMContext):
    markup = await get_currency_markup(aiohttp_session, 0)
    await message.answer(text=render.render_template("convector_currency.html"),
                         reply_markup=markup)


@currency_router.callback_query(ChangePage.filter())
async def all_currency(query: CallbackQuery, callback_data: ChangePage, aiohttp_session: ClientSession):
    markup = await get_currency_markup(aiohttp_session, callback_data.page)
    await query.message.delete()
    await query.message.answer(text=render.render_template("convector_currency.html"),
                               reply_markup=markup)


@currency_router.callback_query(CourseCurrency.filter())
async def start_convector(query: CallbackQuery, callback_data: CourseCurrency, state: FSMContext,
                          aiohttp_session: ClientSession):
    await state.set_state(CurrencyStates.currency)
    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    url += "date_req?=" + str(today)
    res = await fetch_xml(aiohttp_session, url)
    await state.update_data(currency=get_course(res, callback_data.name))
    await state.set_state(CurrencyStates.count)
    await query.message.answer(text=render.render_template("count_money.html"))


@currency_router.message(CurrencyStates.count)
async def end_convector(message: Message, state: FSMContext):
    await state.update_data(count=float(message.text))
    data = await state.get_data()
    await message.answer(text=f"{round(data.get('count') / data.get('currency'), 2)}")
    await state.clear()
