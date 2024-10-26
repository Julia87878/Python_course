import json
from json import JSONDecodeError
from pathlib import Path


def get_financial_transactions(path: Path) -> list:
    """Функция чтения JSON - файла,которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                financial_transactions = json.load(file)
            except JSONDecodeError:
                print("Ошибка декодирования JSON-файла.")
                return []
        if not isinstance(financial_transactions, list):
            print("Ошибка: несписок.")
            return []
        return financial_transactions
    except FileNotFoundError:
        print("Ошибка: фaйл не найден.")
        return []
