from bs4 import BeautifulSoup
from aiohttp import ClientSession


async def fetch_xml(session: ClientSession, url: str) -> BeautifulSoup:
    async with session.get(url) as response:
        xml_content = await response.text()
        soup = BeautifulSoup(xml_content, features='lxml')
        return soup

