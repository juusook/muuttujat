class Pet:
  def __init__(self, name, breed, owner, species):
    self._saying = None
    self.name = name
    self.breed = breed
    self.owner = owner
    self.species = species


  @property
  def saying(self):
    return self._saying

  @saying.setter
  def saying(self, value):
    self._saying = value

  def __str__(self):
    return f"Name: {self.name.capitalize()}; Breed: {self.breed.capitalize()}"


class Owner:
  def __init__(self, name: str, address: str, phone: str, dog=None, saying=None):
    self.name = name
    self.address = address
    self.phone = phone
    self.dog = None
    self.saying = None

  def set_dog(self, dog):
      self.dog = dog

  def __str__(self):
    return f"Name: {self.name.capitalize()}; Address: {self.address}; Phone: {self.phone}"


class Dog(Pet):
    def __init__(self, name, breed, owner):
        super().__init__(name, breed, owner, species='dog')


kevin = Owner('Kevin', 'Museokatu 29', '0408659123', None)
scooby = Dog('Scooby', 'Great Dane', kevin)
# kevin.dog = scooby # set pet

kevin.set_dog(scooby)
print("Kevin's dog's info =>", kevin.dog)

marc = Owner('Marc Maron', 'Los Angeles, California', 'unknown', None)
print(marc.name, f'Dog: {marc.dog}')
scooby.saying = 'BARK BARK BABY'

print(f'{kevin.dog.name} says', kevin.dog.saying)

#print(f'{marc.name} says', marc.saying)

print(scooby.species)