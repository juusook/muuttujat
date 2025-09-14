'''pituus = int(input("anna pituus: "))
on_sopiva = 170 <= pituus <= 180

if on_sopiva:
    print(f"{pituus}cm on hyväksytty pituus!")
else:
    print(f"{pituus}cm ei ole hyväksytty pituus!")'''



'''pituus = int(input("anna pituus: "))

if 170 <= pituus <= 180:
    print(f"{pituus}cm on hyväksytty pituus!")
else:
    print(f"{pituus}cm ei ole hyväksytty pituus!")'''



while True:
    pituus = int(input("Anna pituus: "))

    if 170 <= pituus <= 180:
        print(f"{pituus}cm on sopiva pituus")
        break
    else:
        print(f"{pituus}cm ei ole sopiva pituus")