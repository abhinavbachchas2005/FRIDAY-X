import json
import os


class MemoryManager:

    def __init__(self):

        self.file = "backend/memory.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, memories):

        with open(self.file, "w") as f:
            json.dump(memories, f, indent=4)

    def remember(self, text):

        memories = self.load()

        memories.append(text)

        self.save(memories)

    def get_memories(self):

        return self.load()

    def forget(self, index):

        memories = self.load()

        if 0 <= index < len(memories):
            memories.pop(index)
            self.save(memories)

    def clear(self):

        self.save([])