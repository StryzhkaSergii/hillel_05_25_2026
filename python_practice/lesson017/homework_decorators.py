import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()


def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Виклик функції: {func.__name__}")
        logger.info(f"Аргументи: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        logger.info(f"Результат: {result}")

        return result

    return wrapper


@log_decorator
def add(a, b):
    return a + b


@log_decorator
def multiply(a, b):
    return a * b


print(add(5, 3))
print(multiply(4, 6))



#Декоратор, який перехоплює винятки

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as error:
            logger.error(f"Помилка у функції {func.__name__}: {error}")
            return None

    return wrapper


@exception_handler
def divide(a, b):
    return a / b


print(divide(10, 2))
print(divide(10, 0))