correct_user = "python"
correct_password = "rules"
max_attempts = 5
attempt = 0

while attempt < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_user and password == correct_password:
        print("Welcome")
        break
    else:
        attempt += 1
        if attempt == max_attempts:
            print("Access denied")
        else:
            print("Incorrect password. Please try again.")