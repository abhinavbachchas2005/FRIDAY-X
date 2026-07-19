from datetime import datetime
import os


def show_time():
    now = datetime.now()
    print()
    print("Current Time")
    print("----------------------")
    print(now.strftime("%I:%M:%S %p"))


def show_date():
    today = datetime.now()
    print()
    print("Today's Date")
    print("----------------------")
    print(today.strftime("%d %B %Y"))


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")