class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


auto = Car("Tesla Model X", 300, 12)
print(f"Color: {auto.color}, \
Vehicle name: {auto.name}, \
Speed: {auto.max_speed},\
Mileage: {auto.mileage}")
