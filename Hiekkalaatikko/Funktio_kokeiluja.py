correct_username = "python"
correct_password = "rules"


def käyttäjä_tunnus():
    tries = 0
    max_tries = 3

    while tries < max_tries:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        if entered_username == correct_username and entered_password == correct_password:
            print("Welcome in")
            break

        else:
            print("incorrect username or password")
            tries += 1
            print("try " + str(tries) + ".")
    print("Too many failed attempts. Access denied")
    return


käyttäjä_tunnus()