import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7654869756478768", "7654 86** **** 8768"),
        ("7386963477868564", "7386 96** **** 8564"),
        ("", "Некорректный номер карты"),
        ("743876483976487398", "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        ("73654108430135874305", "**4305"),
        ("", "Некорректный номер счета"),
        ("7438764839764873984876", "Некорректный номер счета"),
    ],
)
def test_get_mask_account(account: str, expected: str) -> None:
    assert get_mask_account(account) == expected
