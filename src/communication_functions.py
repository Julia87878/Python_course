from src.processing import filter_by_state, sort_by_date
from src.readers import get_transactions_csv, get_transactions_excel
from src.transactions_description import get_transactions_by_search_string
from src.utils import get_financial_transactions

json_file = get_financial_transactions(r"C:\Users\Julie\PycharmProjects\Lesson_ Poetry\data\operations.json")
csv_file = get_transactions_csv(r"C:\Users\Julie\PycharmProjects\Lesson_ Poetry\data\transactions.csv")
excel_file = get_transactions_excel(r"C:\Users\Julie\PycharmProjects\Lesson_ Poetry\data\transactions_excel.xlsx")


def get_transactions_from_file(user_format: str) -> list[dict]:
    """Функция выбора формата файла для получения информации о транзакциях пользователем"""
    transactions_from_file = [{}]
    while True:
        if user_format == "1":
            print("Для обработки выбран JSON-файл.")
            transactions_from_file = json_file
            break
        elif user_format == "2":
            print("Для обработки выбран CSV-файл.")
            transactions_from_file = csv_file
            break
        elif user_format == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions_from_file = excel_file
            break
        else:
            print("Такого пункта меню в списке нет, попробуйте выбрать необходимый пункт меню еще раз.")
            continue
    return transactions_from_file


def filter_transactions_by_state(transactions_from_file: list[dict]) -> list[dict]:
    """Функция выбора статуса для фильтрации банковских операций"""
    filtered_transactions = [{}]
    while True:
        user_state = (
            input(
                """Введите статус, по которому необходимо выполнить фильтрацию.\n
         Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n"""
            )
            .strip()
            .upper()
        )
        if user_state == "EXECUTED":
            print("Операции отфильтрованы по статусу: EXECUTED")
            filtered_transactions = filter_by_state(transactions_from_file, state_1="EXECUTED")
            break
        elif user_state == "CANCELED":
            print("Операции отфильтрованы по статусу: CANCELED")
            filtered_transactions = filter_by_state(transactions_from_file, state_1="CANCELED")
            break
        elif user_state == "PENDING":
            print("Операции отфильтрованы по статусу: PENDING")
            filtered_transactions = filter_by_state(transactions_from_file, state_1="PENDING")
            break
        else:
            print(f"Статус операции {user_state} недоступен")
            continue
    return filtered_transactions


def make_assortment_by_date(filtered_transactions: list[dict]) -> list[dict]:
    """Функция, которая уточняет у пользователя делать ли фильтрацию по дате и тип сортировки"""
    user_sort_date = input("Отсортировать операции по дате? Да/Нет").strip().lower()
    if user_sort_date == "да":
        user_type_sort = (
            input("Отсортировать по возрастанию или по убыванию? по возрастанию/ по убыванию").strip().lower()
        )
        if user_type_sort == "по возрастанию":
            results_assortment_by_date = sort_by_date(filtered_transactions, False)
            return results_assortment_by_date
        elif user_type_sort == "по убыванию":
            results_assortment_by_date = sort_by_date(filtered_transactions, True)
            return results_assortment_by_date
    elif user_sort_date == "нет":
        results_assortment_by_date = filtered_transactions
        return results_assortment_by_date


def filter_by_currency_rub(results_assortment_by_date: list[dict], user_format: str) -> list:
    """Функция, которая уточняет у пользователя фильтровать по валюте операции и фильтрует"""
    user_rub_transactions = input("Выводить только рублевые транзакции? Да/Нет").strip().lower()
    if user_rub_transactions == "да":
        if user_format == "1":
            results_by_currency = []
            for tran in results_assortment_by_date:
                if tran.get("operationAmount").get("currency").get("code") == "RUB":
                    results_by_currency.append(tran)
            return results_by_currency
        elif user_format == "2" or user_format == "3":
            results_by_currency = []
            for tran in results_assortment_by_date:
                if tran.get("сurrency_code") == "RUB":
                    results_by_currency.append(tran)
            return results_by_currency
    elif user_rub_transactions == "нет":
        results_by_currency = results_assortment_by_date
        return results_by_currency


def filter_by_certain_word(results_by_currency: list) -> list:
    """Функция, которая уточняет у пользователя фильтровать ли операции
    по определенному слову в описании и фильтрует"""
    user_filter_word = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").strip().lower()
    )
    if user_filter_word == "да":
        user_certain_word = (
            input("Напишите слово, по которому необходимо отфильтровать список транзакций:").strip().lower()
        )
        results_filter_by_certain_word = get_transactions_by_search_string(results_by_currency, user_certain_word)
        return results_filter_by_certain_word
    elif user_filter_word == "нет":
        results_filter_by_certain_word = results_by_currency
        return results_filter_by_certain_word
