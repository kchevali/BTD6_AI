import logging
from typing import TextIO
from bot_log_fmt import LogFormatter
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

class BotLogger(logging.Logger):
    def __init__(self, name:str, level:int=logging.DEBUG) -> None:
        super().__init__(name, level)

        ch: logging.StreamHandler[TextIO] = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(LogFormatter())
        self.addHandler(ch)

def main() -> None:
    logger: BotLogger = BotLogger('test', logging.DEBUG)
    logger.debug("This is a debug")
    logger.info("This is a info")
    logger.warning("This is a warning")
    logger.error("This is a error")
    logger.critical("This is a critical")

if __name__ == '__main__':
    main()