def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    elif not isinstance(age, int):
        raise TypeError("Введіть цифру")

try:
    user_age = "hi"
    check_age(user_age)
    print(f"Ваш вік: {user_age}")
# except ValueError as ve:
#     print(f"Помилка: {ve}")
# except TypeError as e:
#     print(e)
finally:
    print("We can see this")

print("Code goes next")