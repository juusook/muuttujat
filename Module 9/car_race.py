import random

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.maximum_speed = random.randint(100, 200)
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


def race():
    cars = []
    for i in range(1, 11):
        car = Car(f"ABC-{i}")
        cars.append(car)

    race_run = True
    while race_run:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

        for car in cars:
            if car.travelled_distance > 10000:
                winner = car
                race_run = False
                break

    #lambda c: missä c on lamda funktion muuttuja
    cars.sort(key=lambda c: c.travelled_distance, reverse=True)
    return cars


race_results = race()
print(f"Race completed! {len(race_results)} cars participated.")

for i, car in enumerate(race_results[:3]):
    print(f"{i+1}. {car.license_plate}: {car.travelled_distance:.1f} km (speed: {car.current_speed} km/h)")

winner = race_results[0]
print(f"\nWinner: {winner.license_plate} with {winner.travelled_distance:.1f} km!")