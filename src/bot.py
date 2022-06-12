from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import  API

bot = Bot(token=API)
dp = Dispatcher(bot)
@dp.message_handler()
async def start_command(message: types.Message):
#     chat_id = message.chat.id  #  for check user id
#     tex = "Hello"
#     sent_message = await bot.send_message(chat_id=chat_id, text=tex)
#     print(sent_message.to_python())
    


executor.start_polling(dp)