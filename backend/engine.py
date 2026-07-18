from command import CommandHandler

class Engine:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        # Boot sequence...
        print("Welcome, Boss.")

        # Start the command console
        self.command_handler.start() contri