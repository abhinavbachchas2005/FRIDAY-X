from datetime import datetime


class CommandRouter:

    def __init__(self, memory):
        self.memory = memory

    def execute(self, raw_command):
        command = raw_command.lower().strip()

        if command == "hello":
            return "Hello Boss! How can I help you?"

        elif command == "time":
            return datetime.now().strftime("%I:%M:%S %p")

        elif command == "show memory":
            data = self.memory.show()

            if data:
                output = "\nSaved Memories:\n"
                for key, value in data.items():
                    output += f"{key} : {value}\n"
                return output.strip()

            return "Memory is empty."

        elif command.startswith("remember "):
            parts = raw_command.split(maxsplit=2)

            if len(parts) != 3:
                return "Usage: remember <key> <value>"

            key = parts[1]
            value = parts[2]

            self.memory.remember(key, value)
            return f"✅ Remembered '{key}'."

        elif command.startswith("recall "):
            parts = raw_command.split(maxsplit=1)

            if len(parts) != 2:
                return "Usage: recall <key>"

            key = parts[1]
            value = self.memory.recall(key)

            if value is None:
                return "❌ I don't remember that."

            return value

        elif command.startswith("forget "):
            parts = raw_command.split(maxsplit=1)

            if len(parts) != 2:
                return "Usage: forget <key>"

            self.memory.forget(parts[1])
            return "🗑 Memory deleted."

        elif command == "help":
            return """
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
"""

        return "❌ Unknown command. Type 'help'."