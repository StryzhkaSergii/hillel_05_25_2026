def even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number

# Приклад використання
for num in even_numbers(10):
    print(num)


#Генератор чисел Фібоначчі до N
def fibonacci(n):
    a, b = 0, 1

    while a <= n:
        yield a
        a, b = b, a + b

# Приклад використання
for num in fibonacci(50):
    print(num)