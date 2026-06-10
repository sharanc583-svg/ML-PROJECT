import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
	
LOGS_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOGS_FILE,
    level=logging.INFO
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
	datefmt="%Y-%m-%d %H:%M:%S"
)


def get_logger():
	"""Create and return a configured logger."""
	logger = logging.getLogger(name=__name__)
	if not logger.handlers:
		logger.setLevel(level)
		handler = logging.StreamHandler()
		formatter = logging.Formatter(
			"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
		)
		handler.setFormatter(formatter)
		logger.addHandler(handler)
	return logger


# module-level default logger
logger = get_logger()

