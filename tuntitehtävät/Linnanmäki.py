pituus = int(input("Anna pituutesi: "))

if pituus >= 195:
    print("Saat mennä kaikkiin laitteisiin paitsi kirnuun. Olet liian pitkä!")
elif pituus >= 140:
    print("Saat mennä kaikkiin laitteisiin!")
elif pituus >= 100:
    print("Saat mennä lastenlaitteisiin!")
else:
    print("Mee kotiin!")