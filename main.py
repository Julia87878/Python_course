from typing import Any

from src.communication_functions import (
    filter_by_certain_word,
    filter_by_currency_rub,
    filter_transactions_by_state,
    get_transactions_from_file,
    make_assortment_by_date,
)
from src.widget import get_date, mask_account_card


def main() -> Any:
    """Функция, которая отвечает за основную логику проекта с пользователем
    и связывает функциональности между собой."""


user_format = (
    input(
        """Программа: Привет! Добро пожаловать в программу работы
        с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла\n"""
    )
    .strip()
    .lower()
)

transactions_from_file = get_transactions_from_file(user_format)
print(transactions_from_file)

filtered_transactions = filter_transactions_by_state(transactions_from_file)
print(filtered_transactions)

results_assortment_by_date = make_assortment_by_date(filtered_transactions)
print(results_assortment_by_date)

results_by_currency = filter_by_currency_rub(results_assortment_by_date, user_format)
print(results_by_currency)
if not results_by_currency:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

results_filter_by_certain_word = filter_by_certain_word(results_by_currency)
print(results_filter_by_certain_word)

if not results_filter_by_certain_word:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
else:
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(results_filter_by_certain_word)}")
    for r in results_filter_by_certain_word:
        print(f"{get_date(r.get("date"))} {r.get("description")}")
        if r.get("description") == "Открытие вклада":
            print(f"{mask_account_card(r.get("to"))}")
            if user_format == "1":
                print(
                    f"Сумма:{(r.get("operationAmount").get("amount"))} {r.get("operationAmount").get("currency").get("name")}"
                )
            elif user_format == "2" or user_format == "3":
                print(f"Сумма:{r.get("amount")} {r.get("currency_code")}")
        else:
            print(f"{mask_account_card(r.get("from"))} -> {mask_account_card(r.get("to"))}")
            if user_format == "1":
                print(
                    f"Сумма:{(r.get("operationAmount").get("amount"))} {r.get("operationAmount").get("currency").get("name")}"
                )
            elif user_format == "2" or user_format == "3":
                print(f"Сумма:{r.get("amount")} {r.get("currency_code")}")


if __name__ == "__main__":
    main()
