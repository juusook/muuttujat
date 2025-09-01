user = "python"
password = "rules"

annettu_user = input("Enter username: ")
annettu_password = input("Enter password: ")
counter = 0

while (annettu_user != user or annettu_password != password) and counter < 4:
    print("Access denied")
    counter += 1
    annettu_user = input("Enter username: ")
    annettu_password = input("Enter password: ")

print("Welcome")