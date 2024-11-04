import json
from json import JSONDecodeError

# logging.basicConfig(
# level=logging.DEBUG,
# format="%(asctime)s - %(filename)s - %(levelname)s: - %(message)s",
# filename="../logs/utils.log",
# filemode="w",
# )

# logger = logging.getLogger("utils")


def get_financial_transactions(path: str) -> list:
    """Функция чтения JSON - файла,которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                financial_transactions = json.load(file)
                # logger.info("Успешное чтение файла с данными.")
            except JSONDecodeError:
                print("Ошибка декодирования JSON-файла.")
                # logger.error("Ошибка декодирования JSON-файла.")
                return []
        if not isinstance(financial_transactions, list):
            print("Ошибка: несписок.")
            # logger.error("Ошибка: несписок.")
            return []
        return financial_transactions
    except FileNotFoundError:
        print("Ошибка: фaйл не найден.")
        # logger.error("Ошибка: фaйл не найден.")
        return []
