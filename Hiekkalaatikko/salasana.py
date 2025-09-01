'''#oikeat tunnukset ja yrityskertat
correct_username = "python"
correct_password = "rules"
max_attempts = 5

for attempt in range(1, max_attempts +1): #max_attempts + 1 offset
    #kysytään käyttäjätunnus
    username = input("Enter username: ")
    password = input("Enter password: ")

    #verrataan oikeisiin
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        if attempt == max_attempts:
            print("Access denied")
        else:
            print("Incorrect password")'''



