syote = input("Enter a number (or press Enter to quit):")
smallest_number = syote
largest_number = syote

if syote == "":
    pass
else:
    number = float(syote)
    smallest_number = number
    largest_number = number

while syote != "":
        syote = input("Enter a number (or press Enter to quit): ")
        if syote == "":
            break
        number = float(syote)

        if number < smallest_number:
            smallest_number = number
        if number > largest_number:
            largest_number = number
    
print(f"Smallest numer: {smallest_number} Largest number: {largest_number}")