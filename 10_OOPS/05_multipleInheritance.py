class Battery:
    def battery_infro(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "this is engine"
class e3lectricCar(Battery,Engine):
    pass
mycar = e3lectricCar();
print(mycar.engine_info())