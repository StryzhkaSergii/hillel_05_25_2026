import unittest
import sys
import logging.config
import os

from constants import BASE_PROJECT_PATH

config_file_path = os.path.join(BASE_PROJECT_PATH, "logging_config.ini") # BASE_PROJECT_PATH + logging_config.ini with correct /
logging.config.fileConfig(config_file_path) #звідси буде братись файл конфігурації
sys.path.insert(0, BASE_PROJECT_PATH)

from python_practice.lesson12.function import factorial
logger = logging.getLogger("root")

class FactorialNegativeTests(unittest.TestCase):

    def test_factorial_negative_number(self):
        expected_error_message = "You have to use 0 or positive numbers. You put -5"
        logger.info(f"We expect to get ValueError in this test with message {expected_error_message}")
        with self.assertRaises(ValueError) as value_error:
            factorial(-5)
        exception = value_error.exception
        actual_error_message = exception.args[0]
        self.assertEqual(expected_error_message, actual_error_message, msg="Wrong error appeared!!")

    def test_factorial_not_number(self):
        with self.assertRaises(TypeError):
            logger.info(f"We expect to get TypeError in this test")
            factorial("Hello")

if __name__ == "__main__":
    unittest.main(verbosity=2)