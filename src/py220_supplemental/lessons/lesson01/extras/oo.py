class Vehicle:
    def __init__(self):
        self.wheels = 4

    def move(self):
        print("Moving...")


class Car(Vehicle):
    def __init__(self):
        # super().__init__()
        self.passengers = True

    """def move(self):
        print("Moving fast")"""


vehicle = Vehicle()
print(vehicle.move())
print(vehicle.wheels)

car = Car()
print(car.passengers)
print(car.wheels)
car.move()
