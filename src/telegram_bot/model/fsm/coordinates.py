from typing import NamedTuple

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.base import BaseStorage, StorageKey


class CoordinatesStates(StatesGroup):
    latitude = State()
    longitude = State()

