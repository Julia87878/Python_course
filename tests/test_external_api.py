from unittest.mock import patch

import pytest

from src.external_api import get_transaction_amount


@pytest.fixture
def trans() -> dict:
    return {
        "id": 15948212,
        "state": "EXECUTED",
        "date": "2018-12-23T11:47:52.403285",
        "operationAmount": {"amount": "47408.20", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "МИР 8665240839126074",
        "to": "Maestro 3000704277834087",
    }


@pytest.fixture
def trans_2() -> dict:
    return {
        "id": 692008409,
        "state": "CANCELED",
        "date": "2019-02-14T17:38:09.910336",
        "operationAmount": {"amount": "37044.95", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Classic 4610247282706784",
        "to": "Счет 63229171188548882700",
    }


@patch("src.external_api.requests.get")
def test_get_transaction_amount(mock_get, trans):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 47408.2},
        "info": {"timestamp": 1729549022, "rate": 96.797323},
        "date": "2024-10-21",
        "result": 4588986.848249,
    }
    assert get_transaction_amount(trans) == 4588986.848249


def test_get_transaction_amount_2(trans_2):
    assert get_transaction_amount(trans_2) == 37044.95
