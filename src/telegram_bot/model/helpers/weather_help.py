import json
from dataclasses import dataclass
from datetime import datetime
from json import JSONDecodeError
from typing import TypeAlias, NamedTuple, Literal
from enum import Enum
import ssl
import urllib.request

Celsius: TypeAlias = int


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


class WeatherType(str, Enum):
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
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


class CantGetCoordinates(Exception):
    "Программа не смогла получить корректных координат"


def get_weather(coordinates: Coordinates) -> Weather:
    openweather_response = _get_openweather_response(
        longitude=coordinates.longitude,
        latitude=coordinates.latitude
    )
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(latitude: float, longitude: float) -> str:
    ssl.create_default_context = ssl._create_unverified_context
    url =

def format_weather(weather: Weather) -> str:
    return f"""{weather.city}, температура {weather.temperature}°C, {weather.weather_type}
    Восход: {weather.sunrise.strftime("%H:%M")}
    Закат: {weather.sunset.strftime("%H:%M")}
    """


def _parse_openweather_response(open_weather_response: str) -> Weather:
    try:
        open_weather_dict: dict = json.loads(open_weather_response)
    except JSONDecodeError:
        pass
        # raise ApiServiceError
    return Weather(
        temperature=_parse_temperature(open_weather_dict),
        weather_type=_parse_weather_type(open_weather_dict),
        sunrise=_parse_sun_time(open_weather_dict, "sunrise"),
        sunset=_parse_sun_time(open_weather_dict, "sunset"),
        city=_parse_city(open_weather_dict)
    )


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict["main"]["temp"])


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        pass
    #   raise ApiServiceError
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return weather_types
    # raise ApiServiceError


def _parse_sun_time(
        openweather_dict: dict,
        time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])


def _parse_city(openweather_dict: dict) -> str:
    return openweather_dict["name"]
