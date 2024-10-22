import json
import os
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.utils import get_financial_transactions


@pytest.fixture
def path_name():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return path_to_file


@patch("builtins.open")
def test_get_financial_transactions(mock_open: MagicMock, path_name: Path) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_financial_transactions(path_name) == [{"test": "test"}]


@patch("builtins.open")
def test_get_financial_transactions_not_list(mock_open: MagicMock, path_name: Path) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps({"test": "test"})
    assert get_financial_transactions(path_name) == []


@pytest.fixture
def path_name_2():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_2.json")
    return path_to_file


def test_get_financial_transactions_incorrect_data(path_name_2: Path) -> None:
    assert get_financial_transactions(path_name_2) == []


@pytest.fixture
def path_name_3():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_3.json")
    return path_to_file


def test_get_financial_transactions_file_not_found(path_name_3: Path) -> None:
    assert get_financial_transactions(path_name_3) == []
