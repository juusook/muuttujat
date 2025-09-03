import random
N = input("Anna pisteiden määrä: ")
n = 0
count = 0

while n != N:
    x = random.randint(-100, 100) / 100
    y = random.randint(-100, 100) / 100

    if x**2 + y**2 < 1:
        n += 1
    count += 1
pi_likiarvo = 4*N/n

print("Piin likiarvo on:", pi_likiarvo)
#vastaus on x**2 + y**2 < 1