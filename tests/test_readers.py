import os
from unittest.mock import patch

import pandas as pd
import pytest

from src.readers import get_transactions_csv, get_transactions_excel


@pytest.fixture
def test_df():
    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"],
    }
    return pd.DataFrame(test_dict)


@pytest.fixture
def path_name_1():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
    return path_to_file


@patch("src.readers.pd.read_csv")
def test_get_transactions_csv(mock_read, test_df, path_name_1):
    mock_read.return_value = test_df
    result = get_transactions_csv(path_name_1)
    expected = test_df.to_dict(orient="records")
    assert result == expected


@pytest.fixture
def path_name_2():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")
    return path_to_file


@patch("src.readers.pd.read_excel")
def test_get_transactions_excel(mock_read, test_df, path_name_2):
    mock_read.return_value = test_df
    result = get_transactions_excel(path_name_2)
    expected = test_df.to_dict(orient="records")
    assert result == expected


@pytest.fixture
def path_name_3():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_2.csv")
    return path_to_file


def test_get_transactions_csv_file_not_found(path_name_3: str) -> None:
    assert get_transactions_csv(path_name_3) == []


@pytest.fixture
def path_name_4():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel_2.xlsx")
    return path_to_file


def test_get_transactions_excel_file_not_found(path_name_4: str) -> None:
    assert get_transactions_excel(path_name_4) == []
