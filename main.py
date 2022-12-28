import user_interface
import controller
import logging

logger = logging.getLogger("phonebookApp")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("phonebook.log", encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info("Program started")
controller.open_db()
user_interface.open()
logger.info("Program closed")
