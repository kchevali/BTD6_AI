import logging
from typing import Optional

class LogFormatter(logging.Formatter):

    grey: str = "\x1b[38;20m"
    blue: str = "\x1b[34;20m"
    green: str = "\x1b[32;20m"
    yellow: str = "\x1b[33;20m"
    red: str = "\x1b[31;20m"
    bold_red: str = "\x1b[31;1m"
    reset: str = "\x1b[0m"
    format_str: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    line_format_str: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d in %(funcName)s)"

    level_formats: dict[int, str] = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: blue + format_str + reset,
        logging.WARNING: yellow + line_format_str + reset,
        logging.ERROR: red + line_format_str + reset,
        logging.CRITICAL: bold_red + line_format_str + reset
    }

    def format(self, record:logging.LogRecord) -> str:
        log_fmt: Optional[str] = self.level_formats.get(record.levelno)
        formatter: logging.Formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)