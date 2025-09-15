class Vehicle:
    def __init__(self, brand, speed, fuel):
        self.brand = brand
        self.speed = speed
        self.fuel = fuel

    def __str__(self):
        return f"{self.brand} can go {self.speed} and has {self.fuel} fuel"
    
    def move(self):
        return f"{self.brand} is moving at {self.speed} mph"
    
class Car(Vehicle):
    def __init__(self, brand, speed, fuel, doors, engine):
        super().__init__(brand, speed, fuel)
        self.doors = doors
        self.engine = engine

    def move(self):
        return f"{self.brand} car is driving at {self.speed} mph with a {self.engine} engine"
    
    def __str__(self):
        return f"{self.brand} car can go {self.speed} mph, has {self.doors} doors, a {self.fuel} tank, and has a {self.engine} engine"
    
    class Bike(Vehicle):
        def __init__(self, brand, speed, bike_type, has_gears):
            super().__init__(brand, speed)
            self.bike_type = bike_type
            self.has_gears = has_gears
    
    def move(self):
        return f"{self.brand} bike {self.bike_type} is pedaling at {self.speed} mph with/without gears"
    
    def __str__(self):
        return f"{self.brand} {self.bike_type} bike can go {self.speed} and has {self.has_gears}"