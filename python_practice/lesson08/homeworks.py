import math

def unique_symbols(text):
    return len(set(text)) > 10


def contains_h(word):
    return "h" in word.lower()


def get_strings(lst):
    return [item for item in lst if isinstance(item, str)]


def even_sum(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    return total


def get_test_name(log):
    if "TestCase: " not in log:
        return ""

    return log.split("TestCase: ")[1]

def circle_area(radius):
    return math.pi * radius ** 2


def rectangle_area(width, height):
    return width * height


def sum_numbers(string):
    numbers = string.split(",")

    total = 0

    for number in numbers:
        total += int(number)

    return total


def calculate_total_area(area1, area2):
    return area1 + area2

def average(nums):
    return sum(nums) / len(nums)