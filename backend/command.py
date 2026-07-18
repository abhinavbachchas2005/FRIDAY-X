from command_registry import CommandRegistry


class CommandHandler:

    def __init__(self):
        self.registry = CommandRegistry()

        self.registry.register("help", self.show_help)
        self.registry.register("about", self.show_about)
        self.registry.register("version", self.show_version)

    def start(self):
        print("\nFRIDAY X is ready, Boss.")
        print("Type 'help' to see available commands.")
        print()

        while True:

            command = input("FRIDAY > ").strip().lower()

            if command == "":
                continue

            if command == "exit":
                print("\nGoodbye, Boss.")
                break

            self.registry.execute(command)

    def show_help(self):
        print("\nAvailable Commands")
        print("------------------")
        print("help")
        print("about")
        print("version")
        print("exit")
        print()

    def show_about(self):
        print("\nFRIDAY X")
        print("Personal AI Assistant")
        print()

    def show_version(self):
        print("\nVersion 0.1.0")
        print()