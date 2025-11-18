class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
    pass
School_bus=Bus("Volvo","120","11")
print("Vehicle name:",School_bus.name)
print("Vehicle maximum speed:",School_bus.max_speed)
print("Mileage:",School_bus.mileage)