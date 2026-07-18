class CommandRegistry:

    def __init__(self):
        self.commands = {}

    def register(self, command, function):
        self.commands[command] = function

    def execute(self, command):
        if command in self.commands:
            self.commands[command]()
        else:
            print("❌ Unknown command. Type 'help'.")