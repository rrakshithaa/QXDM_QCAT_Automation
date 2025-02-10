import logging
import os
import datetime

from pyexpat.errors import messages


class Logger:
    _logger_instance = None

    @classmethod
    def get_logger(cls):
        if cls._logger_instance is None:
            # Directory and log file setup
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_____%H-%M-%S')
            log_dir = "logs"
            log_file = f"application_{timestamp}.log"
            log_file_path = os.path.join(log_dir, log_file)

            # Ensure the log directory exists
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
                print(f"Log directory '{log_dir}' created successfully.")

            # Create and configure the logger
            logger = logging.getLogger("Logs")
            logger.setLevel(logging.DEBUG)

            # File handler for logging to file
            file_handler = logging.FileHandler(log_file_path)
            console_handler = logging.StreamHandler()

            # Set logging levels for handlers
            file_handler.setLevel(logging.DEBUG)
            console_handler.setLevel(logging.DEBUG)

            # Log format
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers to the logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

            cls._logger_instance = logger

        return cls._logger_instance


# Create logger instance
logger = Logger.get_logger()
