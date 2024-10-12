from functools import wraps


def log(filename=""):
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if filename:
                try:
                    result = func(*args, **kwargs)
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok.")
                    return result
                except Exception as e:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
            else:
                try:
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} ok.")
                    return result
                except Exception as e:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator
