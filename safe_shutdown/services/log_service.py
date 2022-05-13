import logging


class LogService:
    def __init__(self) -> None:
        logging.basicConfig(
            format="%(asctime)s %(message)s",
            datefmt="%Y/%m/%d %H:%M:%S",
            level=logging.INFO,
            filename="/var/log/safe-shutdown.log",
            filemode="a",
        )
        self.logger = logging.getLogger("safe_shutdown")

    def write(self, object):
        self.logger.info(object)
