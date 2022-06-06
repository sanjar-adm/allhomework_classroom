class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus (Vehicle):
    def seating_capacity(self, capacity = 50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

a = Bus('AUDI' , 220,1111111)
print(a.seating_capacity())