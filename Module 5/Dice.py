import random

heitot = []
rolls = int(input("How many dice to roll: "))

for n in range(rolls):
    heitot.append(random.randint(1,6))
    print(heitot)

print(f"Sum of the dice: {sum(heitot)}")
