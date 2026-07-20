from command_registry import CommandRegistry
from memory import MemoryManager
from core.utils import show_time, show_date, clear_screen


class CommandHandler:

    def __init__(self):

        self.registry = CommandRegistry()
        self.memory = MemoryManager()

        self.registry.register("help", self.show_help)
        self.registry.register("about", self.show_about)
        self.registry.register("version", self.show_version)

        self.registry.register("time", show_time)
        self.registry.register("date", show_date)
        self.registry.register("clear", clear_screen)
        self.registry.register("cls", clear_screen)

        self.registry.register("memories", self.show_memories)
        self.registry.register("clear memories", self.clear_memories)

    def start(self):

        print()
        print("FRIDAY X is ready, Boss.")
        print("Type 'help' to see available commands.")

        while True:

            command = input("\nFRIDAY > ").lower().strip()

            if command == "exit":
                print("\nGoodbye, Boss.")
                break

            if command.startswith("remember "):

                text = command[9:]

                if text.strip():
                    self.memory.remember(text)
                    print("✓ Memory saved.")
                else:
                    print("Nothing to remember.")

                continue

            if command.startswith("forget "):

                try:
                    index = int(command.split()[1]) - 1
                    self.memory.forget(index)
                    print("✓ Memory removed.")
                except:
                    print("Invalid memory number.")

                continue

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
        print("remember <text>")
        print("memories")
        print("forget <number>")
        print("clear memories")
        print("exit")

    def show_about(self):

        print()
        print("FRIDAY-X")
        print("Your Personal AI Assistant")

    def show_version(self):

        print()
        print("FRIDAY-X Version 0.1.0")

    def show_memories(self):

        memories = self.memory.get_memories()

        if not memories:
            print("\nNo memories found.")
            return

        print("\nSaved Memories")
        print("----------------------")

        for i, item in enumerate(memories, start=1):
            print(f"{i}. {item}")

    def clear_memories(self):

        self.memory.clear()

        print("✓ All memories cleared.")