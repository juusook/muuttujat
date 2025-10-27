#tehtävä 1
class Car:
    def __init__(self, license_plate, maximum_speed=142):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    #tehtävä 2
    def accelerate(self, accelerate):
        self.current_speed += accelerate
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed
        return

    #tehtävä 3
    def drive(self, travelled_hours = 0):
        travelled_hours += travelled_hours
        self.travelled_distance += travelled_hours * self.current_speed
        return

car = Car("ABC-123", 142)
print(f"Initial distance: {car.travelled_distance} km")
car.accelerate(30)
car.drive(1.5)
print(f"Current speed: {car.current_speed} km/h")
car.accelerate(30)
car.drive(1.5)
print(f"Current speed: {car.current_speed} km/h")
car.accelerate(90)
car.drive(1.5)
print(f"Current speed: {car.current_speed} km/h")
print(f"Distance after driving hours at 60 km/h: {car.travelled_distance} km")
