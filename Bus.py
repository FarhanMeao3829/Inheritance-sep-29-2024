class Vehicle:
    
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
        
        
    def details(self):
        print(f"Name : {self.name}, Speed : {self.max_speed}, Milage : {self.milage}")
        
        
class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)

print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Milage:", School_bus.milage)

School_bus.details()