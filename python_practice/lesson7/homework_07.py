# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier * number <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            break
            # Enter the action to take if the result is greater than 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(a, b):
    """Обчислює суму двох чисел"""
    return a + b

# Тестування
print(sum_two_numbers(5, 3))      # 8
print(sum_two_numbers(-2, 10))    # 8
print(sum_two_numbers(0.5, 1.5))  # 2.0

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)

# Тестування
print(average([1, 2, 3, 4, 5]))     # 3.0
print(average([10, 20, 30]))        # 20.0
print(average([100]))               # 100.0

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]

# Тестування
print(reverse_string("Hello"))      # olleH
print(reverse_string("Python"))     # nohtyP
print(reverse_string("12345"))      # 54321

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    if not words:
        return None
    return max(words, key=len)

# Тестування
print(longest_word(["cat", "elephant", "dog"]))           # elephant
print(longest_word(["a", "ab", "abc", "abcd"]))           # abcd
print(longest_word(["Python", "Java", "JavaScript"]))     # JavaScript

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(main_string, sub_string):

    return main_string.find(sub_string)

string1 = "Hello, world!"
string2 = "world"
print(find_substring(string1, string2))  # 7

string1 = "The quick brown fox jumps over the lazy dog"
string2 = "cat"
print(find_substring(string1, string2))  # -1

# task 7
def calculate_total_area(area1, area2):
    return area1 + area2

black_sea_area = 436402  # км²
azov_sea_area = 37800    # км²

total_area = calculate_total_area(black_sea_area, azov_sea_area)
print("Разом Чорне та Азовське моря займають", total_area, "км².")

# task 8
def calculate_total_price(period_months, payment_amount):
    """Обчислює загальну вартість комп'ютера"""
    return period_months * payment_amount

months = 1.5 * 12  # 1.5 року = 18 місяців
monthly_payment = 1179  # грн
total_price = calculate_total_price(months, monthly_payment)

print(f"Вартість комп'ютера: {int(total_price)} грн.")

# task 9
def filter_strings(lst):
    result = []
    for item in lst:
        if isinstance(item, str):
            result.append(item)
    return result

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = filter_strings(lst1)
print(lst2)

# task 10
def sum_even_numbers(input_list):
    result = 0
    for num in input_list:
        if num % 2 == 0:
            result += num
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum_even_numbers(numbers)
print(total)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""