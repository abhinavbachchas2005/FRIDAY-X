import time

from core.config import config
from core.logger import logger

class BootManager:
    def boot(self):
        for step in config.boot_steps:
            logger.info(step)
            print(step)
            time.sleep(0.5)

        logger.info("System Boot Complete")