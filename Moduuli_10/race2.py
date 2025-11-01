import random

class Car:
    def __init__(self, license_plate, maximum_speed=142):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, accelerate):
        self.current_speed += accelerate
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        return

    def drive(self, travelled_hours = 0):
        self.travelled_distance += self.current_speed * travelled_hours
        return


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)


    def print_status(self):
        for car in self.cars:
            print(f"license plate: {car.license_plate} | {car.current_speed} km/h | {car.travelled_distance} km")



    def race_finished(self):
        run = False
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                run = True
        return run






cars = []
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)
print(f"Race created: {race.name} ({race.distance} km)")
print(f"Cars participating: {len(race.cars)}")

print(f"\nRace finished initially: {race.race_finished()}")

for hour in range(5):
    race.hour_passes()
    if hour == 2:
        print(f"After {hour+1} hours, race finished: {race.race_finished()}")
