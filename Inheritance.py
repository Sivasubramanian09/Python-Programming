class Vechile:
    def general_usage(self):
        print("General use: Transportation")
        
class car(Vechile):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True
        
    def specific_usage(self):
        print("Specific use: commute to work,vacation with family")
        
    class Motorcycle(Vechile)