import random

heitot = []                                     #luo tyhjän listan
rolls = int(input("How many dice to roll: "))   #pytää syötettä ja tekee luokkamuunnoksen

for _ in range(rolls):
    heitot.append(random.randint(1,6))    #heittää noppaa ja lisää listan loppuun
    print(heitot)

print(f"Sum of the dice: {sum(heitot)}") #sum() summaa termit yhteen
