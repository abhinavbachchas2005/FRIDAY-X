from dataclasses import dataclass, field

@dataclass
class AppConfig:
    app_name: str = "FRIDAY X"
    version: str = "0.1.0"
    owner_title: str = "Boss"
    wake_word: str = "Friday"
    debug: bool = True

    boot_steps: list[str] = field(default_factory=lambda: [
        "Loading configuration...",
        "Initializing logger...",
        "Checking system...",
        "Loading modules...",
        "Preparing AI engine...",
    ])

config = AppConfig()
