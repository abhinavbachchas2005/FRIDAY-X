from memory.memory import Memory
from datetime import datetime

memory = Memory()


def show_help():
    print("""
Available Commands:
-------------------
help                 - Show available commands
hello                - Greet FRIDAY
time                 - Show current time
remember <k> <v>     - Store information
recall <k>           - Recall information
forget <k>           - Delete information
show memory          - Display all saved memories
exit                 - Exit FRIDAY
""")


def main():
    print("=" * 50)
    print("        FRIDAY-X v0.7.0")
    print("=" * 50)
    print("System Boot Complete.")
    print("Welcome, Boss!")
    print("Type 'help' to see available commands.\n")

    while True:
        raw_command = input("FRIDAY > ").strip()

        if not raw_command:
            continue

        command = raw_command.lower()

        # Exit
        if command == "exit":
            print("Goodbye, Boss!")
            break

        # Help
        elif command == "help":
            show_help()

        # Greeting
        elif command == "hello":
            print("Hello Boss! How can I help you?")

        # Time
        elif command == "time":
            print(datetime.now().strftime("%I:%M:%S %p"))

        # Remember
        elif command.startswith("remember "):
            parts = raw_command.split(maxsplit=2)

            if len(parts) == 3:
                key = parts[1]
                value = parts[2]
                memory.remember(key, value)
                print(f"✅ Remembered '{key}'.")
            else:
                print("Usage: remember <key> <value>")

        # Recall
        elif command.startswith("recall "):
            parts = command.split(maxsplit=1)

            if len(parts) == 2:
                key = parts[1]
                value = memory.recall(key)

                if value is not None:
                    print(value)
                else:
                    print("❌ I don't remember that.")
            else:
                print("Usage: recall <key>")

        # Forget
        elif command.startswith("forget "):
            parts = command.split(maxsplit=1)

            if len(parts) == 2:
                memory.forget(parts[1])
                print("🗑 Memory deleted.")
            else:
                print("Usage: forget <key>")

        # Show Memory
        elif command == "show memory":
            data = memory.show()

            if data:
                print("\nSaved Memories:")
                for key, value in data.items():
                    print(f"{key} : {value}")
            else:
                print("Memory is empty.")

        # Unknown command
        else:
            print("❌ Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()