import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: - %(message)s",
    filename="../logs/masks.log",
    filemode="w",
)

logger = logging.getLogger("masks")


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    if len(card_number) < 16 or len(card_number) > 16:
        logger.error("Некорректный номер карты.")
        return "Некорректный номер карты"
    else:
        mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
        logger.info("Успешная маскировка номера банковской карты")
        return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    if len(account) < 20 or len(account) > 20:
        logger.error("Некорректный номер счета.")
        return "Некорректный номер счета"
    else:
        mask_account = "**" + account[16:]
        logger.info("Успешная маскировка номера банковского счета")
        return mask_account


if __name__ == "__main__":
    print(get_mask_card_number("8765987683675476"))
    print(get_mask_card_number("876598768367547"))
    print(get_mask_account("73654108430135874305"))
    print(get_mask_account("7365410843013587430556"))
