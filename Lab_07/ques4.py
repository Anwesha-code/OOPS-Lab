# Create a class Vehicle with a method info() that prints "This is a vehicle". Inherit Car from Vehicle and add a method car_info() to print "This is a car". Further, create another subclass ElectricCar that inherits from Car and adds a method battery_info() to print "This car has a battery." Demonstrate how multilevel inheritance works by calling all methods from an ElectricCar object.

class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a car")

class ElectricCar(Car):
    def battery_info(self):
        print("This car has a battery")

electric_car = ElectricCar()
electric_car.info()           
electric_car.car_info()       
electric_car.battery_info()    
