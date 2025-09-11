import random
N = int(input("Anna pisteiden määrä: "))
n = 0
count = 0

while count < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(n)
    if x**2 + y**2 < 1:
        n += 1
    count += 1
pi_likiarvo = 4*N/n

print("Piin likiarvo on:", pi_likiarvo)
#vastaus on x**2 + y**2 < 1