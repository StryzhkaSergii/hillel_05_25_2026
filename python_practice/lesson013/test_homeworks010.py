import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from homework_10 import log_event


class TestLogEvent(unittest.TestCase):

    LOG_FILE = os.path.join(os.path.dirname(__file__), "login_system.log")

    def test_success_log(self):
        log_event("admin", "success")

        with open(self.LOG_FILE, "r") as file:
            content = file.read()

        self.assertIn("Username: admin", content)
        self.assertIn("Status: success", content)
        self.assertIn("INFO", content)

    def test_warning_log(self):
        log_event("user", "expired")

        with open(self.LOG_FILE, "r") as file:
            content = file.read()

        self.assertIn("Username: user", content)
        self.assertIn("Status: expired", content)
        self.assertIn("WARNING", content)

    def test_error_log(self):
        log_event("guest", "failed")

        with open(self.LOG_FILE, "r") as file:
            content = file.read()

        self.assertIn("Username: guest", content)
        self.assertIn("Status: failed", content)
        self.assertIn("ERROR", content)

    def test_logs_are_appended(self):
        # Отримати кількість рядків на початку тесту
        if os.path.exists(self.LOG_FILE):
            with open(self.LOG_FILE, "r") as file:
                lines_before = len([line for line in file if line.strip()])
        else:
            lines_before = 0

        # Перший виклик
        log_event("user1", "success")
        # Другий виклик
        log_event("user2", "failed")

        with open(self.LOG_FILE, "r") as file:
            lines_after = len([line for line in file if line.strip()])

        # Обидва логи повинні бути в файлі
        with open(self.LOG_FILE, "r") as file:
            content = file.read()

        self.assertIn("user1", content)
        self.assertIn("user2", content)

        # Перевірити, що додалось рівно 2 нових рядки
        self.assertEqual(lines_after - lines_before, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)