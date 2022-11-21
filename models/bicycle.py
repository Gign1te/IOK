
class Bicycle:
    def __init__(self, name, number_of_gears, velocity, gear):
        self.name = name
        self.number_of_gears = number_of_gears
        self.velocity = velocity
        self.gear = gear

    def change_gear(self):
        self.gear += 1