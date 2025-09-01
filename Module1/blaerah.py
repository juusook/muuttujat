'''import random

# Tehdään kolme satunnaista numeroa ja liitetään ne merkkijonoksi
tulos = "".join(str(random.randint(0, 9)) for _ in range(3))

print(tulos)  # esim. 582'''


#Listat ja niiden tulostaminen
nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

print(nimet[3])
print(nimet[1])
print(nimet[-2])
print(nimet[1:3])
print(nimet[2:])
print(nimet)

nimet.append("Juuso")
nimet.remove("Viivi")

print(nimet)


for luku in range(1,5):
    print(luku)