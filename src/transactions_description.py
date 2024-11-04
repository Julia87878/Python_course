import re
from collections import Counter


def get_transactions_by_search_string(transactions: list[dict], search_string: str) -> list:
    """функция, возвращающая список словарей с данными о банковских операциях,
    у которых в описании есть определенная строка поиска."""
    new_list = []
    for transaction in transactions:
        description_value = transaction.get("description", "")
        if isinstance(description_value, str) and re.findall(search_string, description_value, flags=re.IGNORECASE):
            new_list.append(transaction)
    return new_list


def count_operations_by_category(transactions: list[dict], categories: list) -> dict:
    """функция принимает список словарей с данными о банковских операциях
    и список категорий операций, а возвращает словарь, в котором ключи —
    это названия категорий, а значения — это количество операций в каждой категории"""
    list_operations = []
    count = 0
    for transaction in transactions:
        for category in categories:
            if category == transaction.get("description", ""):
                list_operations.append(transaction.get("description", ""))
                count = Counter(list_operations)
    return count
