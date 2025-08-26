inches = float(input("Enter length in inches (negative value to quit): "))
inch = 2.54

while inches >= 0.:
    print(f"{inches} inches is {inches * inch :.2f} centimeters.")
    inches = float(input("Enter length in inches (negative value to quit): "))
print("Program ended.")