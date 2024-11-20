from vehicle import Vehicle

class Car(Vehicle):
    
    def __int__(self, make, model, year, num_doors):
        super().__int__(make, model, year)
        self.num_doors = num_doors
        
    def __str__(self):
        return super().__str__()+ " Doors: "+ str(self.num_doors)