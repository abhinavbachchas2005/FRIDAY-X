import json
import os


class Memory:
    def __init__(self):
        self.file = os.path.join(os.path.dirname(__file__), "memory.json")
        self.data = {}
        self.load()

    def load(self):
        if os.path.exists(self.file):
            try:
                with open(self.file, "r") as f:
                    self.data = json.load(f)
            except Exception:
                self.data = {}
        else:
            self.save()

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=4)

    def remember(self, key, value):
        self.data[key] = value
        self.save()

    def recall(self, key):
        return self.data.get(key)

    def forget(self, key):
        if key in self.data:
            del self.data[key]
            self.save()

    def show(self):
        return self.data