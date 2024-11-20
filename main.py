from vehicle import Vehicle
from car import Car

if __name__ == "__main__":
    
    #create an instance of the Vechicle class
    black_car = Vehicle("Tesla", "Model 3", 2018)
    red_car = Vehicle("Toyota", "Camry", 2023)
    real_car = Car()
    
    all_vehicles = Vehicle.get_all_vehicles()
    for vehicle in all_vehicles:
        print(vehicle)
    