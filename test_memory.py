from memory.memory import Memory

mem = Memory()

mem.remember("name", "Abhinav")
mem.remember("language", "Python")

print(mem.recall("name"))
print(mem.show())

mem.forget("language")

print(mem.show())