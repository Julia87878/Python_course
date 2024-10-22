import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> Any:
    """Функция конвертации"""
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    if code == "RUB":
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        headers = {"apikey": "4J7PtKIvS0xhEYfu91zaceFRjT79LPru"}
        response = requests.get(url, headers=headers)
        result = response.json()
        return result["result"]
