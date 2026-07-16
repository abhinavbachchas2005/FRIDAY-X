"""
FRIDAY X Engine
"""

from core.config import config
from core.logger import logger


class Engine:
    def __init__(self):
        logger.info("Engine created")

    def start(self):
        logger.info("Starting FRIDAY X")

        self.load_configuration()
        self.load_logger()
        self.boot()

        logger.info("FRIDAY X started successfully")

    def load_configuration(self):
        logger.info("Configuration loaded")

    def load_logger(self):
        logger.info("Logger initialized")

    def boot(self):
        print("=" * 50)
        print(config.app_name)
        print(f"Version {config.version}")
        print("System Boot Complete")
        print(f"Welcome, {config.owner_title}.")
        print("=" * 50)