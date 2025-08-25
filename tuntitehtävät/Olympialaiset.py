given_year = int(input("Anna vuosi: "))

if given_year == 2020:
    print("Ei ollut poikkeuksellisesti koronan takia")
elif given_year == 2021:
    print("Oli olympiavuosi poikkeuksellisesti")
elif given_year % 4 == 0 and not 2020:
    print("Oli olympialaisvuosi.")
else:
    print("ei ollut olympiavuosi")