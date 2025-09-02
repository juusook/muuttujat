from Hiekkalaatikko.salasana import correct_password, correct_username, max_attempts

correct_password
correct_username
max_attempts
attempt = 0

while attempt < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempt += 1
        if attempt == max_attempts:
            print("Access denied")
        else:
            print("Incorrect username or password. Try again")