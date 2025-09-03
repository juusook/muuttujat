import random
target = 6

def roll_dice():
    return random.randint(1,6) #palauttaan random numeron

heitto = 0                           #muuttuja heiton silmäluvulle
counter = 0                          #laskee heittojen määrän
while heitto != target:
    heitto = roll_dice()             #kutsutaan funktio roll_dice ja määritetään se variableen heitto
    counter += 1
    print(heitto)                     #tulostetaan heitto

print()
print(f"heittojen määrä oli {counter}") #tulostaa heittojen määrän