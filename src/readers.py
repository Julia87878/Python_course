import pandas as pd


def get_transactions_csv(path_to_file: str) -> list:
    """Функция для считывания финансовых операций из CSV"""
    try:
        transactions_csv_frame = pd.read_csv(path_to_file, delimiter=";")
        transactions_csv_list_dict = transactions_csv_frame.to_dict(orient="records")
        return transactions_csv_list_dict
    except FileNotFoundError:
        print("Ошибка: фaйл не найден.")
        return []


def get_transactions_excel(path_to_file: str) -> list:
    """Функция для считывания финансовых операций из Excel"""
    try:
        transactions_excel_frame = pd.read_excel(path_to_file)
        transactions_excel_list_dict = transactions_excel_frame.to_dict(orient="records")
        return transactions_excel_list_dict
    except FileNotFoundError:
        print("Ошибка: фaйл не найден.")
        return []
