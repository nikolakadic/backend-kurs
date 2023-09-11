class Car:
    def __init__(self, fuel, brand, power):
        self.fuel = fuel
        self.brand = brand
        self.power = power
    
    def refuel(self, fuel):
        self.fuel += fuel
