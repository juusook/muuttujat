import random
tahkojen_maara = int(input("Anna tahkojen määrä: "))
target = tahkojen_maara

def roll_dice():
    return random.randint(1,tahkojen_maara) #palauttaan random numeron

heitto = 0                           #muuttuja heiton silmäluvulle
while heitto != target:
    heitto = roll_dice()             #kutsutaan funktio roll_dice ja määritetään se variableen heitto
    print(heitto)                    #tulostetaan heitto