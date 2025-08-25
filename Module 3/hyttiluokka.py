'''LUX on parvekkeellinen hytti yläkannella.
A on ikkunallinen hytti autokannen yläpuolella.
B on ikkunaton hytti autokannen yläpuolella.
C on ikkunaton hytti autokannen alapuolella '''

hyttiluokka = input("Mikä hyttiluokka: ")
LUX = ("LUX on parvekkeellinen hytti yläkannella.")
A = ("A on ikkunaton hytti autokannen yläpuolella")
B = ("B on ikkunaton hytti autokannen yläpuolella")
C = ("C on ikkunaton hytti autokannen alapuolella")

if hyttiluokka == "LUX" or "lux":
    print(LUX)
elif hyttiluokka == "A" or "a":
    print(A)
elif hyttiluokka == "B" or "b":
    print(B)
elif hyttiluokka == "C" or "c":
    print(C)
else:
    print("Väärä hyttiluokka!")