import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
# print(sys.path)
# print(pathlib.Path(__file__).parent.parent.parent)
from python_practice.lesson12.function import some_function

def sum_two_numbers(a, b):
    return a + b

class MyTest(unittest.TestCase):

    def test_example(self):
        actual_result = sum_two_numbers(1,3)
        expected_result = 4
        self.assertEqual(expected_result, actual_result)

    def test_example_second(self):
        actual_result = some_function(1,3)
        expected_result = 5

        self.assertEqual(expected_result, actual_result)
        # assert actual_result == expected_result

    # def test_example_list(self):
    #     actual_result = [{"Name":"Alex", "Age":"30", "Position":"AQA"},
    #                      {"Name":"Den", "Age":"25", "Position":"QA"},
    #                      {"Name":"Ivan", "Age":"40", "Position":"Programer"},]
    #     expected_result = [{"Name":"Den", "Age":"30", "Position":"AQA"},
    #                      {"Name":"Den", "Age":"40", "Position":"AQA"},
    #                      {"Name":"Ivan", "Age":"40", "Position":"QA"},]
    #     self.assertEqual(expected_result, actual_result)
    #     # assert actual_result == expected_result

if __name__ == "__main__":
    unittest.main(verbosity=2)