from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number: str) -> str:
    """Функция,которая обрабатывает информацию о картах и счетах"""
    if type_number[:4] == "Счет":
        account = type_number[5:]
        mask_account = get_mask_account(account)
        type_mask_account = "Счет" + " " + mask_account
        return type_mask_account
    else:
        card_number = type_number[-16:]
        mask_card_number = get_mask_card_number(card_number)
        type_number_list = type_number.split()
        type_list = []
        for element in type_number_list:
            if element.isalpha():
                type_list.append(element)
        str_type_list = " ".join(type_list)
        type_mask_number = str_type_list + " " + mask_card_number
        return type_mask_number


def get_date(date_1: str) -> str:
    """Функция, которая меняет формат даты"""
    if len(date_1) == 26:
        date_2 = date_1[8:10] + "." + date_1[5:7] + "." + date_1[:4]
        return date_2
    else:
        return "Некорректный формат даты"
