numbers = []
syote = input("Enter a number (or press enter to quit): ")

while syote != "":
    luku = int(syote)
    numbers.append(luku)
    syote = input("Enter a number (or press enter to quit): ")

numbers.sort(reverse=True)
top_numbers = numbers [:5]

print("The greatest numbers: ")
for number in top_numbers:
    print(number)