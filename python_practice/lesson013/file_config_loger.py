import logging.config
import os

from constants import BASE_PROJECT_PATH

config_file_path = os.path.join(BASE_PROJECT_PATH, "logging_config.ini") # BASE_PROJECT_PATH + logging_config.ini with correct /
logging.config.fileConfig(config_file_path) #звідси буде братись файл конфігурації

logger = logging.getLogger("sampleLogger")
new_custom_logger = logging.getLogger("customLogger")

logger.debug('This is DEBUG log level')
logger.info('This is INFO log level')
logger.error('This is ERROR log level')

new_custom_logger.critical("This is CRITICAL log level")