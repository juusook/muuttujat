'''
nimet = ["Jaakko", "Reetta", "Kari"]
toiset_nimet = ["Pekka", "Anni", "Siina"]

nimet.extend(toiset_nimet)
nimet.remove("Jaakko")

print(nimet)'''

def ikä_tulostus():
    for nimi, ikä in age.items():
        print(nimi + " on " + ikä)
    return

age = {"Jaakko": "32",
       "Ahmed": "16",
       "Sanni": "38"}

ikä_tulostus()


'''nimet = ("Rosa", "Jossu", "Kassu", "Mikko", "Olli") #joukko, ei voi muokata
for nimi in nimet:
    print(nimi)'''