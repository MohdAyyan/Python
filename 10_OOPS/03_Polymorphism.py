class Car:
    total_car = 0;
    def __init__(self,brand,model):
        self.brand = brand;
        self.model = model;
        Car.total_car += 1;
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "diesel and petrol"
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size;
    def fuel_type(self):
        return "Electric charge"

# my_car = Car("Tata","Safari");
# print(my_car.full_name())     

   
my_tesla = ElectricCar("Tesla","Model S","85KWH");
safari = Car("tata","safari");
print(safari.fuel_type())
# print(my_tesla.battery_size)
print(Car.total_car)

# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.full_name())
