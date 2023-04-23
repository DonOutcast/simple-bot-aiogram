from bs4 import BeautifulSoup


def get_all_currency(soup_result: BeautifulSoup) -> list[list[str]]:
    return [currency.find("name").text for currency in soup_result.find_all("valute")]


def get_course(soup_result: BeautifulSoup, name_of_currency: str):
    for valute in soup_result.find_all("valute"):
        if valute.find("name").text == name_of_currency:
            currency_value = valute.find("value").text.replace(',', '.')
            currency_nominal = valute.find("nominal").text
            value = float(currency_value) / int(currency_nominal)
            return round(value, 2)
