import random
number = random.randint(1,10)
print(number)

guess = int(input("Guess a number between (1-10): "))

while guess != number:
    if guess < number:
        print("too low")
        guess = int(input("Guess a number between (1-10): "))
    elif guess > number:
        print("too high")
        guess =  int(input("Guess a number between (1-10): "))
print("correct")