class Elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = self.bottom_floor

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"Kerros {self.current_floor}")

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"Kerros {self.current_floor}")

    def go_to_floor(self, chosen_floor):
        while True:
            if chosen_floor == self.current_floor:
                break
            elif self.current_floor < chosen_floor:
                self.floor_up()
            elif self.current_floor > chosen_floor:
                self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_number = num_elevators
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(top_floor, bottom_floor))

    def run_elevator(self,e_num, target_floor):
        elevator = self.elevators[e_num]
        elevator.go_to_floor(target_floor)

    def fire_alarm(self):
        for i in self.elevators:
            i.go_to_floor(self.bottom_floor)



# Test Building with multiple elevators
building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 3)
building.run_elevator(2, 8)
building.fire_alarm()