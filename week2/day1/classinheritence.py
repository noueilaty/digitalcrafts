class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def run(self):
        print(self.name + " is running.")

    def walk(self):
        print(self.name + " is walking")

# Parent class inheritance
class Cheetah(Animal):
    def __init__(self):
        # parents constructor (initializer):
        super(Cheetah, self), __init__('Cheetah', 'Cats')
        self.name = ""

print('-------------------')

class Car(object):
    def __init(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("Starting the gas car")

class ElectricCar(Car):
    def __init__(self):
        super(ElectricCar, self).__init__('Tesla', 'X')

    # overriding the start method from the super/parent/base class:
    def start(self):
        print("Starting the electic car")


electric_car = ElectricCar()
print(electric_car.make)
print(electric_car.model)
electric_car.start()
