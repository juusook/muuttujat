numbers = []
syote = input("Enter a number (or press enter to quit): ")

while syote != "":              #looppi silloin kun syöte on muu kuin tyhjä rivi
    luku = int(syote)           #muuttaa syötteen stringistä numeroksi
    numbers.append(luku)        #lisää listaan
    syote = input("Enter a number (or press enter to quit): ") #uusi syöte, looppi alkaa alusta

numbers.sort(reverse=True) #kääntää listan suuruusjärjestyksessä suurimmasta pienimpään
top_numbers = numbers [:5] #valitsee listan viisi ensimmäistä

print("The greatest numbers: ")
for number in top_numbers: #käy läpi listan top_numbers ja luo variablen number, jotta voi tulostaa omille riveilleen
    print(number)