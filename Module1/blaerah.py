import random

# Tehdään kolme satunnaista numeroa ja liitetään ne merkkijonoksi
tulos = "".join(str(random.randint(0, 9)) for _ in range(3))

print(tulos)  # esim. 582

