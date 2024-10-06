def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    if len(card_number) < 16 or len(card_number) > 16:
        return "Некорректный номер карты"
    else:
        mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
        return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    if len(account) < 20 or len(account) > 20:
        return "Некорректный номер счета"
    else:
        mask_account = "**" + account[16:]
        return mask_account
