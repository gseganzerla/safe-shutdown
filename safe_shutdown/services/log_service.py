import logging
from pathlib import Path

class LogService:
    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO, filename=f"{Path.home()}/.safe_shutdown.log")
        self.logger = logging.getLogger()

    def write(self, object):
        self.logger.info(object)
