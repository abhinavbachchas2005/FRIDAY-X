from memory.memory import Memory
from backend.router import CommandRouter

memory = Memory()
router = CommandRouter(memory)


def main():
    print("=" * 50)
    print("        FRIDAY-X v0.8.0")
    print("=" * 50)
    print("System Boot Complete.")
    print("Welcome, Boss!")
    print("Type 'help' to see available commands.\n")

    while True:
        command = input("FRIDAY > ").strip()

        if not command:
            continue

        if command.lower() == "exit":
            print("Goodbye, Boss!")
            break

        response = router.execute(command)
        print(response)


if __name__ == "__main__":
    main()