class Dog:
    created = 0

    def __init__(self, name, birth_year, bark='bark-bark'):
        self.name = name
        self.birth_year = birth_year
        self.bark = bark
        Dog.created = Dog.created + 1


    def barking(self, times):
        for _ in range(times):
            print(self.bark)
        return

class DayCare:
    def __init__(self):
        self.dogs  = []

    def dog_in(self, dog):
        self.dogs.append(dog)
        print(dog.name + ' kirjattu sisään')

    def dog_out(self, dog):
        self.dogs.remove(dog)
        print(dog.name + ' has left the daycare')

    def greet_dogs(self):
        for dog in self.dogs:
            dog.barking(1)

    def list_dogs(self):
        for dog in self.dogs:
            print(dog.name)


dog1 = Dog('Rekku', 1997)
koira2 = Dog('Lassie', 1987, 'Aargh!')
koira3 = Dog('Snoopy', 1970)


print(f"Koiran nimi on {koira2.name} ja hän on syntynyt vuonna {koira2.birth_year}.")
dog1.barking(3)
koira2.barking(2)
print(f'Koiria on nyt {Dog.created}.')

hoitola = DayCare()

hoitola.dog_in(dog1)
hoitola.dog_in(koira2)
hoitola.dog_in(koira3)
hoitola.greet_dogs()

hoitola.dog_out(dog1)
hoitola.list_dogs()