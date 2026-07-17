class CommandHandler:

    def start(self):
        print("\nFRIDAY X is ready, Boss.")
        print("Type 'help' to see available commands.")
        print()

        while True:

            command = input("FRIDAY > ").strip().lower()

            if command == "help":
                self.show_help()

            elif command == "about":
                self.show_about()

            elif command == "version":
                self.show_version()

            elif command == "exit":
                print("\nGoodbye, Boss.")
                break

            elif command == "":
                continue

            else:
                print("Unknown command.")

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