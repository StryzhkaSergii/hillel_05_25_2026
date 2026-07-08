def sum_numbers(string):
    try:
        numbers = string.split(",")
        total = 0

        for num in numbers:
            total += int(num)

        return total

    except ValueError:
        return "Не можу це зробити!"


lst = [
    "1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3"
]

for item in lst:
    print(sum_numbers(item))