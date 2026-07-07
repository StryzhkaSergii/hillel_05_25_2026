class TooLargeValueError(Exception):
    def __init__(self, value, limit):
        self.value = value
        self.limit = limit
        message = f"Значення {value} перевищує ліміт {limit}"
        super().__init__(message)

# Приклад використання власного виключення
try:
    limit = 100
    user_input = int(input("Введіть число: "))

    if user_input > limit:
        raise TooLargeValueError(user_input, limit)
    else:
        print("Дякую! Ви ввели припустиме значення.")
except TooLargeValueError as e:
    print(f"Помилка: {e}")
except ValueError:
    print("Помилка: Будь ласка, введіть ціле число.")