import logging
import os

from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("ekyc")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | %(message)s"
)

# Main log

app_handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=5 * 1024 * 1024,
    backupCount=5
)

app_handler.setFormatter(formatter)

# Error log

error_handler = RotatingFileHandler(
    "logs/error.log",
    maxBytes=5 * 1024 * 1024,
    backupCount=5
)

error_handler.setLevel(logging.ERROR)

error_handler.setFormatter(formatter)

# Console

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

logger.addHandler(app_handler)
logger.addHandler(error_handler)
logger.addHandler(console_handler)