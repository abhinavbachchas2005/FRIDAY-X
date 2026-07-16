"""
FRIDAY X Configuration
----------------------
Central configuration for the application.
"""

from dataclasses import dataclass


@dataclass
class AppConfig:
    app_name: str = "FRIDAY X"
    version: str = "0.1.0"
    owner_title: str = "Boss"
    wake_word: str = "Friday"
    debug: bool = True


config = AppConfig()