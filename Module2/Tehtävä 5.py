#Yksi leiviskä (talents) on 20 naulaa.
#Yksi naula (pounds) on 32 luotia.
#Yksi luoti (lots) on 13,3 grammaa.

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

#print(f"The pounds in grams: {(pounds / 32) * 13.3}")
#print(f"The talents in grams: {((talents * 20) * 32) * 13.3}")

total_grams = ((lots * 13.3) + ((pounds * 32) * 13.3) + (((talents * 20) * 32) * 13.3))
kilograms = int(total_grams / 1000)
remaining_grams = round(total_grams % 1000, 2)

print(f"The weight in modern units:\n {kilograms} kilograms and {remaining_grams:.2f} grams.")


