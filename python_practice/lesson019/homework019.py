import logging
from datetime import datetime

# Налаштування логера
logging.basicConfig(
    filename="hb_test.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger()

KEY = "TSTFEED0300|7E3E|0400"

def analyze_heartbeat(filename):
    filtered_log = []

    # Зчитуємо файл
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if KEY in line:
                filtered_log.append(line.strip())

    previous_time = None

    for line in filtered_log:

        # Знаходимо час після "Timestamp "
        start = line.find("Timestamp ")

        if start == -1:
            continue

        time_str = line[start + len("Timestamp "): start + len("Timestamp ") + 8]

        current_time = datetime.strptime(time_str, "%H:%M:%S")

        if previous_time is not None:

            heartbeat = abs((current_time - previous_time).total_seconds())

            # Якщо лог йде у зворотному порядку
            if heartbeat > 3600:
                heartbeat = 86400 - heartbeat

            if 31 < heartbeat < 33:
                logger.warning(
                    f"Heartbeat = {heartbeat:.0f} sec at {time_str}"
                )

            elif heartbeat >= 33:
                logger.error(
                    f"Heartbeat = {heartbeat:.0f} sec at {time_str}"
                )

        previous_time = current_time


analyze_heartbeat("hblog.txt")

print("Аналіз завершено.")
print("Результат записано у файл hb_test.log")