import logging
import xml.etree.ElementTree as ET

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger()


def find_incoming(filename, group_number):
    tree = ET.parse(filename)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is None or number.text != str(group_number):
            continue

        incoming = group.find("timingExbytes/incoming")

        if incoming is None:
            logger.info(
                f"Group {group_number} знайдена, але timingExbytes/incoming відсутній."
            )
            return None

        logger.info(
            f"Group {group_number}: incoming = {incoming.text}"
        )
        return incoming.text

    logger.info(f"Group {group_number} не знайдена.")
    return None


# Приклад виклику
find_incoming("groups.xml", 0)
find_incoming("groups.xml", 1)
find_incoming("groups.xml", 99)