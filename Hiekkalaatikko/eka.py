import random
values = []

throws = int(input("How many times should I throw the dice: "))

for _ in range(throws):
    throw = random.randint(1, 6)
    values.append(throw)

b = 0
for number in values:
    a = number
    b += a

print(f"The sum of rolls is {b}")
