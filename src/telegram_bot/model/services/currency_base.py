import asyncio
import warnings
from aiohttp import ClientSession, ClientTimeout
from bs4 import BeautifulSoup, GuessedAtParserWarning
from datetime import datetime

from lxml import etree
import contextlib

url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}


# response = requests.get(url, params=payload)
# xml = BeautifulSoup(response.content, 'lxml')


# def get_course(name_valute):
#     name_valute = name_valute.split()[1:]
#     name_valute = " ".join(name_valute)
#     all_valutes = xml.find_all("valute")
#     for element in all_valutes:
#         if name_valute.lower() == element.find("name").text.lower():
#             return element.find("value").text
#     else:
#         return "Валюта не найдена!"


async def fetch_xml(session: ClientSession, url: str) -> BeautifulSoup:
    async with session.get(url) as response:
        xml_content = await response.text()
        soup = BeautifulSoup(xml_content, features='lxml')
        return soup


def get_all_currency(soup_result: BeautifulSoup) -> list[str]:
    return [currency.find("name").text for currency in soup_result.find_all("valute")]


async def main():
    session_timeout = ClientTimeout(total=1, connect=1)
    async with ClientSession(timeout=session_timeout) as session:
        url = "http://www.cbr.ru/scripts/XML_daily.asp?"
        today = datetime.today()
        today = today.strftime("%d/%m/%Y")
        url += "date_req?=" + str(today)
        res = await fetch_xml(session, url)
        print(get_all_currency(res))


if __name__ == "__main__":
    asyncio.run(main())
