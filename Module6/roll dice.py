import random
target = 6

def roll_dice():
    return random.randint(1,6) #palauttaan random numeron

heitto = 0                           #muuttuja heiton silmäluvulle
while heitto != target:
    heitto = roll_dice()             #kutsutaan funktio roll_dice ja määritetään se variableen heitto
    print(heitto)                    #tulostetaan heitto