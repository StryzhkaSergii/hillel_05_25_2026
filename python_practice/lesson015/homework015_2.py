import json
import logging

# Налаштування логера
logging.basicConfig(
    filename="json_stryzhka.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger()

def validate_json(filename):
    """Перевіряє, чи є файл валідним JSON."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            json.load(file)
        print(f"{filename} - валідний JSON")

    except json.JSONDecodeError as error:
        logger.error(f"{filename} - невалідний JSON. {error}")
        print(f"{filename} - невалідний JSON")

    except FileNotFoundError as error:
        logger.error(f"{filename} - файл не знайдено. {error}")
        print(f"{filename} - файл не знайдено")

# Список файлів для перевірки
json_files = [
    "localizations_en.json",
    "localizations_ru.json",
    "login.json",
    "swagger.json",
]

for file in json_files:
    validate_json(file)