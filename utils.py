import json
import os
import requests


API_KEY = os.getenv('API_KEY')


def get_currency_rate(currency: str) -> float:
    """Получает курс валюты от API и возвращает его в виде float к рублю"""

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    response = requests.get(url, headers={'apikey': API_KEY})
    response_data = json.loads(response.text)
    rate = response_data["rates"]["RUB"]
    print(len(list(response_data['rates'])))
    return rate


def main(currency):
    """
    Основная функция программы. Получает от пользователя название валюты USD или EUR,
    получает и выводит на экран текущий курс валюты от API. Записывает данные в json файл.
    """
    while True:
        rate = get_currency_rate(currency)

        txt = f"Курс {currency} к рублю: {rate:.2f}"

        return txt


def get_all_currency(currency='RUB'):
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    response = requests.get(url, headers={'apikey': API_KEY})
    response_data = json.loads(response.text)
    rate = list(response_data["rates"])
    return rate


if __name__ == "__main__":
    answer = input()
    print(main(answer))
    print(get_all_currency())
