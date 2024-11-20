# Parent class
class Vechicle:
    
    wheels = 4 #class level atrribute to all objects
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year