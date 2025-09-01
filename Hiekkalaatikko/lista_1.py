'''nimet = []

etunimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while etunimi != "":
    nimet.append(etunimi)
    etunimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for nimi in nimet:
    print (f"Moi, {nimi}!")'''

numerot = [1, 2, 3, 4, 5, 6, 7]
numerot.sort(reverse = True)
print(numerot)
