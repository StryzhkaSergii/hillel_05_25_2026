import logging

file_handler = logging.FileHandler("../../error.log")
file_handler.setLevel(logging.ERROR)
file_formater = logging.Formatter("Custom formater: %(name)s - %(asctime)s -  %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
# Створення конфігурації
logging.basicConfig(level=logging.DEBUG,
                    format='!!!! %(asctime)s - %(lineno)d - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # Виведення в консоль
                        logging.FileHandler('../../example.log'),  # Запис у файл
                        file_handler
                    ])

# Використання логера
logger = logging.getLogger(__name__)

logger.debug('This is DEBUG log level')
logger.info('This is INFO log level')
logger.error('This is ERROR log level')