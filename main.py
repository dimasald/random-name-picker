import random

names = []

name = input("Enter a name (if the name is Q, enter in this first input now): ")
names.append(name)

while True:
    print(names)
    name = input("Any name? (Q to quit and start pick random name): ") 
    names.append(name)
    

    if name == "Q":
        names.remove("Q")
        break


print(names)

name_random = random.choice(names)

print(name_random)

