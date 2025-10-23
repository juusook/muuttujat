syote = input("Anna vuosi(tai paina enter lopettaaksesi): ")
first_year = 1924
vuosi = int(syote)

if vuosi == "":
    pass
elif vuosi < first_year:
    print("Ei ollut, koska talviolympialaiset alkoivat vasta vuonna 1924")
elif (vuosi - first_year) % 4 == 0:
    print("Vuosi on talviolympialaisvuosi")
else:
    print("Vuosi ei ole talviolympialaisvuosi.")
