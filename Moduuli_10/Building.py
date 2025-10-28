class Elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top = top_floor
        self.bottom = bottom_floor
        self.current_floor = self.bottom

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"Kerros {self.current_floor}")

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"Kerros {self.current_floor}")

    def go_to_floor(self, chosen_floor):
        chosen_floor = chosen_floor
        while True:
            if chosen_floor == self.current_floor:
                break
            elif self.current_floor < chosen_floor:
                self.floor_up()
            elif self.current_floor > chosen_floor:
                self.floor_down()

class Building:
    def __init__(self):
        elevators = []
    def run_elevator(self,e_num, index ):
        pass





h = Elevator(10, 1)

h.go_to_floor(5)
h.go_to_floor(1)
h.go_to_floor(10)
h.go_to_floor(9)
h.go_to_floor(1)