import logging
import os

class CommonLogger:
    def __init__(self, name="afwlogs"):
        self.log_file = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs"),"afw.txt")
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # File handler
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers
        if not self.logger.handlers:
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

# Usage in any framework
"""logger = CommonLogger().get_logger()
logger.info("Test started")
logger.error("Element not found")"""
