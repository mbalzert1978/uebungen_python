class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)


Bus_v = Bus("School Volvo", 80, 120000)

print(f"Vehicle Name: {Bus_v.name} Speed:\
     {Bus_v.max_speed} Mileage: {Bus_v.mileage}")
