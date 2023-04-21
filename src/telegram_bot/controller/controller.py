from aiogram import Bot
from aiogram import Dispatcher
from aiogram import exceptions
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommandScopeDefault, MenuButtonWebApp, WebAppInfo
from aiohttp import ClientTimeout
# from aioredis import Redis

from configurate.config import settings

from model.handlers.user import user_router
from model.handlers.echo import echo_router
from model.handlers.admin import admin_router
from model.handlers.weather import weather_router
from model.handlers.back_to_menu import back_to_menu_router
from model.handlers.erro import error_router


from model.middlewares.config import ConfigMiddleware
from model.middlewares.throttling import ThrottlingMiddelware
from model.middlewares.chataction import ChatActionMiddleware
from model.middlewares.aiohttp import AiohttpSessionMiddleware

from model.services import broadcaster


from model.commnad_scope.scopes import SetCommands


# from model.handlers.echo import echo_router
class Controller(object):
    __instance = None
    # redis = Redis()

    bot = Bot(settings.bot_token.get_secret_value(), parse_mode="HTML")
    storage = MemoryStorage
    dp = Dispatcher()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Controller, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True

    def _register_global_middlewares(self, config: settings):
        aiohttp_session_timeout = ClientTimeout(total=1, connect=5)
        self.dp.update.middleware(AiohttpSessionMiddleware(aiohttp_session_timeout))
        self.dp.message.middleware(ChatActionMiddleware())
        self.dp.message.outer_middleware(ConfigMiddleware(config))

    async def _on_startup(self, admin_ids: list[int]):
        await broadcaster.broadcast(self.bot, admin_ids, "Бот запущен!")

    async def main(self):
        routers = [
            admin_router,
            user_router,
            weather_router,
            back_to_menu_router,
            error_router,
        ]
        for router in routers:
            self.dp.include_router(router)
        self._register_global_middlewares(settings)
        try:
            # await self.bot.set_chat_menu_button(
            #     menu_button=MenuButtonWebApp(
            #         type="web_app", text="Открыть веб приложение",
            #         web_app=WebAppInfo(url="https://github.com/DonOutcast/Donbook.github.io"))
            # )
            await self.bot.delete_webhook()
            await self.bot.delete_my_commands()
            await SetCommands(self.bot).set_default_commands()
            bot_commands = await self.bot.get_my_commands()
            for command in bot_commands:
                print(*command)
                # print(command.command, "-", command.description, "-", command.)
            await self._on_startup(settings.admins)
            await self.bot.delete_webhook(drop_pending_updates=True)
            await self.dp.start_polling(self.bot, allowed_updates=self.dp.resolve_used_update_types())
        except exceptions as ex:
            print(ex)
        finally:
            await self.bot.session.close()
