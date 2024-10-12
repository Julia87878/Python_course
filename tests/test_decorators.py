from src.decorators import log


def test_log_1(capsys):
    """Тестирует успешное выполнение функции"""

    @log()
    def addition(a, b):
        return a + b

    result = addition(4, 2)
    assert result == 6


def test_log_2(capsys):
    """Тестирует вывод после ошибки в консоль"""

    @log()
    def subtraction(a, b):
        return a - b

    subtraction(8, "5")
    captured = capsys.readouterr()
    assert captured.out == "subtraction error: TypeError. Inputs: (8, '5'), {}\n"


def test_log_3(capsys):
    """Тестирует вывод после ошибки в консоль"""

    @log()
    def division(a, b):
        return a / b

    division(8, 0)
    captured = capsys.readouterr()
    assert captured.out == "division error: ZeroDivisionError. Inputs: (8, 0), {}\n"


def test_log_4():
    """Тестирует успешное выполнение функции"""

    @log("log.txt")
    def multiplication(a, b):
        return a * b

    result = multiplication(7, 3)
    assert result == 21


def test_log_5():
    """Тестирует запись в файл после успешного выполнения"""

    @log("log.txt")
    def addition(a, b):
        return a + b

    addition(7, 3)
    with open("log.txt", "r", encoding="utf-8") as file:
        logs = file.read()
        assert "addition ok." in logs


def test_log_6():
    """Тестирует запись в файл после ошибки"""

    @log("log.txt")
    def division(a, b):
        return a / b

    division(5, 0)
    with open("log.txt", "r", encoding="utf-8") as file:
        logs = file.read()
        assert "division error: ZeroDivisionError. Inputs: (5, 0), {}" in logs


def test_log_7():
    """Тестирует запись в файл после ошибки"""

    @log("log.txt")
    def addition(a, b):
        return a + b

    addition(5, "3")
    with open("log.txt", "r", encoding="utf-8") as file:
        logs = file.read()
        assert "addition error: TypeError. Inputs: (5, '3'), {}" in logs
