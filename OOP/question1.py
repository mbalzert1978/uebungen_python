class Vehicle:
    max_speed: int
    mileage: float

    def __init__(self, max_speed, mileage) -> None:
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f"Vehicle({self.max_speed}, {self.mileage})"


modelY = Vehicle(
    300,
    12.5
)
print(modelY)
