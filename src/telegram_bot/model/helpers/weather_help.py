from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias, NamedTuple
from enum import Enum

Celsius: TypeAlias = int


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"



@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates):
    pass
