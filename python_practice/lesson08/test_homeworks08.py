import unittest
import math

from python_practice.lesson08.homeworks import (
    unique_symbols,
    contains_h,
    get_strings,
    even_sum,
    get_test_name,
    circle_area,
    rectangle_area,
    sum_numbers,
    calculate_total_area,
    average
)


class TestHomeworks(unittest.TestCase):

# unique_symbols

    def test_unique_symbols_more_than_10(self):
        actual_result = unique_symbols("abcdefghijk")
        expected_result = True

        self.assertEqual(expected_result, actual_result)

    def test_unique_symbols_less_than_10_unique_symbol(self):
        actual_result = unique_symbols("Hello world")
        expected_result = False

        self.assertEqual(expected_result, actual_result)

# contains_h

    def test_contains_h_lowercase(self):
        actual_result = contains_h("hello")
        expected_result = True

        self.assertEqual(expected_result, actual_result)

    def test_contains_h_uppercase(self):
        actual_result = contains_h("House")
        expected_result = True

        self.assertEqual(expected_result, actual_result)

    def test_contains_h_not_found(self):
        actual_result = contains_h("apple")
        expected_result = False

        self.assertEqual(expected_result, actual_result)

# get_strings

    def test_get_strings(self):
        data = ["1", 2, True, "Python", 5.5]

        actual_result = get_strings(data)
        expected_result = ["1", "Python"]

        self.assertEqual(expected_result, actual_result)

    def test_get_strings_empty(self):
        actual_result = get_strings([1, 2, 3])
        expected_result = []

        self.assertEqual(expected_result, actual_result)

# even_sum

    def test_even_sum(self):
        actual_result = even_sum([1, 2, 3, 4, 5, 6])
        expected_result = 12

        self.assertEqual(expected_result, actual_result)

    def test_even_sum_only_odd(self):
        actual_result = even_sum([1, 3, 5])
        expected_result = 0

        self.assertEqual(expected_result, actual_result)

# get_test_name

    def test_get_test_name(self):
        log = "2023-04-27 15:30:45 - TestCase: login_successful"

        actual_result = get_test_name(log)
        expected_result = "login_successful"

        self.assertEqual(expected_result, actual_result)

    def test_get_test_name_not_found(self):
        actual_result = get_test_name("No TestCase")
        expected_result = ""

        self.assertEqual(expected_result, actual_result)

# circle_area

    def test_circle_area_radius_1(self):
        actual_result = circle_area(1)
        expected_result = math.pi

        self.assertEqual(expected_result, actual_result)

    def test_circle_area_radius_5(self):
        actual_result = circle_area(5)
        expected_result = math.pi * 25

        self.assertEqual(expected_result, actual_result)

# rectangle_area

    def test_rectangle_area(self):
        actual_result = rectangle_area(5, 4)
        expected_result = 20

        self.assertEqual(expected_result, actual_result)

    def test_rectangle_area_square(self):
        actual_result = rectangle_area(6, 6)
        expected_result = 36

        self.assertEqual(expected_result, actual_result)

# sum_numbers

    def test_sum_numbers(self):
        actual_result = sum_numbers("1,2,3,4")
        expected_result = 10

        self.assertEqual(expected_result, actual_result)

    def test_sum_numbers_one_number(self):
        actual_result = sum_numbers("15")
        expected_result = 15

        self.assertEqual(expected_result, actual_result)

    def test_sum_numbers_invalid_data(self):
        with self.assertRaises(ValueError):
            sum_numbers("1,a,3")

# calculate_total_area

    def test_calculate_total_area(self):
        actual_result = calculate_total_area(15, 20)
        expected_result = 35

        self.assertEqual(expected_result, actual_result)

    def test_calculate_total_area_zero(self):
        actual_result = calculate_total_area(10, 0)
        expected_result = 10

        self.assertEqual(expected_result, actual_result)

# average

    def test_average(self):
        actual_result = average([2, 4, 6, 8])
        expected_result = 5

        self.assertEqual(expected_result, actual_result)

    def test_average_one_number(self):
        actual_result = average([10])
        expected_result = 10

        self.assertEqual(expected_result, actual_result)

    # def test_average_empty_list(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         average([])


if __name__ == "__main__":
    unittest.main(verbosity=2)