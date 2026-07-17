import logging
import os
import inspect

logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), 'login_system.log'),
    level=logging.INFO,
    format='%(asctime)s - %(message)s - %(levelname)s',
    force=True
)
logger = logging.getLogger()


def log_event(username: str, status: str):
    test_name = "Unknown"

    # Шукаємо у стеку викликів функцію, яка починається з test_
    for frame in inspect.stack():
        if frame.function.startswith("test_"):
            test_name = frame.function
            break
    """
    Логує подію входу в систему.
    username: Ім'я користувача, яке входить в систему.
    status: Статус події входу:
    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed - пароль невірний, логується на рівні error
    """
    log_message = (
        f"Test: {test_name} | Username: {username}, Status: {status}"
    )

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)