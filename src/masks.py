def get_mask_card_number(card_number: int) -> str:
    """Функция, которая маскирует номер банковской карты"""
    str_card_number = str(card_number)
    mask_card_number = str_card_number[:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[12:]
    return mask_card_number


def get_mask_account(account: int) -> str:
    """Функция, которая маскирует номер банковского счета"""
    str_account = str(account)
    mask_account = "**" + str_account[16:]
    return mask_account
