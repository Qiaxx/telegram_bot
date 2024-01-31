import json
import os
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackContext
import requests


API_KEY = os.getenv('API_KEY')


def get_currency_rate(currency: str) -> float:
    """Получает курс валюты от API и возвращает его в виде float к рублю"""

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    response = requests.get(url, headers={'apikey': API_KEY})
    response_data = json.loads(response.text)
    rate = response_data["rates"]["RUB"]
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


if __name__ == "__main__":
    main()