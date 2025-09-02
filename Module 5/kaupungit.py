num_cities = 5
cities = []

for i in range(num_cities):
    given_city = input("Enter the name of a city: ")
    cities.append(given_city)


print()
print("The cities you entered: ")
for city in cities:
    print(city)