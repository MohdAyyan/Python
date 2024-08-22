class Car:
    def __init__(self,brand,model):
        self.__brand = brand;
        self.model = model;
    def get_brand(self):
        return f"{self.__brand} !"
    def full_name(self):
        return f"{self.__brand} {self.model}"
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size;
    
      
my_tesla = ElectricCar("Tesla","Model S","85KWH");

print(my_tesla.__brand)
# print(my_tesla.model)
# print(my_tesla.full_name())
