hyttiluokka = input("Enter the cabin class (LUX, A, B, or C): ")
LUX = "Upper-deck cabin with a balcony."
A = "Above the car deck, equipped with a window."
B = "Windowless cabin above the car deck."
C = "Windowless cabin below the car deck."


if hyttiluokka == "LUX":
    print(LUX)
elif hyttiluokka == "A":
    print(A)
elif hyttiluokka == "B":
    print(B)
elif hyttiluokka == "C":
    print(C)
else:
    print("Invalid cabin class.")