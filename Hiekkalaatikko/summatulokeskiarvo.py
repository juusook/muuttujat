import random
import math
luvut = []
for _ in range(int(input("monta lukua: "))):
    rand = random.randint(1, 10)
    luvut. append(rand)

summa = sum(luvut)
tulo = math.prod(luvut)
keskiarvo = summa/ len(luvut)

print("summa:", summa)
print("tulo:", tulo)
print("keskiarvo", keskiarvo)

print(math.radians(60))
