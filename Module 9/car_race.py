import random

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.maximum_speed = 142
        self.current_speed = 0
        self.travelled_distance = 0
        self.travelled_hours = 0

    def accelerate(self, accelerate):
        self.current_speed += accelerate
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed
        return

    def drive(self, hours = 0):
        self.travelled_hours += hours
        self.travelled_distance += hours * self.current_speed
        return

def make_car():
    cars = []
    for i in range(1, 11):
        car = Car(f"ABC-{i}")
        cars.append(car)





car = Car("ABC-123", 142)
print(f"Initial distance: {car.travelled_distance} km")
car.accelerate(30)
print(f"Current speed: {car.current_speed} km/h")
print(f"Distance after driving hours at 60 km/h: {car.travelled_distance} km")


