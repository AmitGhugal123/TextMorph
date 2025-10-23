from logger import setup_logger  # replace 'your_logger_file' with the name of your logger Python file

# Set up logger
logger = setup_logger()

# Test logs
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")
