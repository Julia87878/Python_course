def filter_by_currency(transactions, currency):
    """Генератор, который фильтрует транзакции по валюте"""
    if transactions == []:
        yield "Нет транзакций"
    else:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions):
    """Генератор, который возвращает описание каждой операции по очереди"""
    if transactions == []:
        yield "Нет транзакций"
    else:
        for transaction in transactions:
            transaction_description = transaction.get("description")
            yield transaction_description


def card_number_generator(start, stop):
    """Генератор, который генерирует номера банковских карт в заданном диапазоне(от 0000 0000 0000 0001
    до 9999 9999 9999 9999"""
    if start < 1 or stop > 9999999999999999:
        yield "Ошибка ввода"
    else:
        for number in range(start, stop + 1):
            number_zero = "0000000000000000"
            card_number_1 = number_zero[: -len(str(number))] + str(number)
            formatted_card_number = (
                f"{card_number_1[:4]} {card_number_1[4:8]} {card_number_1[8:12]} {card_number_1[12:16]}"
            )
            yield formatted_card_number
