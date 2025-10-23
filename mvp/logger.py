import logging
import os
from datetime import datetime

def setup_logger(name="MVPLogger", log_dir="logs", level=logging.INFO):
    """
    Configures a logger that writes to both file and console.
    """
    # Ensure logs directory exists (at root)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    log_path = os.path.join(base_dir, log_dir)
    os.makedirs(log_path, exist_ok=True)

    log_file = os.path.join(log_path, f"log_{datetime.now().strftime('%Y%m%d')}.log")

    # Logger instance
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Formatter
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%Y-%m-%d %H:%M:%S")

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
