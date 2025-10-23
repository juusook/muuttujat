import random

nimet = ["Joonatan ", "Juuso", "Kaarle", "Emmi"]

random.shuffle(nimet)

for i, nimi in enumerate(nimet, start=1):
    print(i, nimi)

#tulostaa 1-10
for i in range(1, 11):
    print(i)