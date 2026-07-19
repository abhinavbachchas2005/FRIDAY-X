from command_registry import CommandRegistry
from core.utils import show_time, show_date, clear_screen

class CommandHandler:

    def __init__(self):

        self.registry = CommandRegistry()

        self.registry.register("help", self.show_help)
        self.registry.register("about", self.show_about)
        self.registry.register("version", self.show_version)

        self.registry.register("time", show_time)
        self.registry.register("date", show_date)
        self.registry.register("clear", clear_screen)
        self.registry.register("cls", clear_screen)

    def start(self):

        print()
        print("FRIDAY X is ready, Boss.")
        print("Type 'help' to see available commands.")

        while True:

            command = input("\nFRIDAY > ").lower().strip()

            if command == "exit":
                print("\nGoodbye, Boss.")
                break

            self.registry.execute(command)

    def show_help(self):

        print()
        print("Available Commands")
        print("----------------------")
        print("help")
        print("about")
        print("version")
        print("time")
        print("date")
        print("clear")
        print("cls")
        print("exit")

    def show_about(self):

        print()
        print("FRIDAY-X")
        print("Your Personal AI Assistant")

    def show_version(self):

        print()
        print("FRIDAY-X Version 0.1.0")