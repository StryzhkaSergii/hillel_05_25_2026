def some_function(a, b):
    print(a + b)
    return a + b

def factorial(n):
    if n < 0:
        raise ValueError(f"You have to use 0 or positive numbers. You put {n}")

    if type(n) != int:
        raise  TypeError(f"Only int allowed, you put {type(n)}")

    if n == 0:
        return 1

    else:
        return n * factorial(n-1)