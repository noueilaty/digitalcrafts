# Classes and Objects

# A class is a blueprint of what you're defining.

class Car:
# This method initializes the class:
    def __init__(self, make, model):
        # Self is the current instance of the object you're trying to create:
        self.make = make
        self.model = model
        self.noOfCylinders = 4
        # If you don't include 'Self', it doesn't pass itself to the object you're creating:
    def start(self):
        print("Starting Car")

    def honk(self):
        print("BEEP!")

    def turn(self, direction):
        print("Car is turning {}".format(direction))

# An object of the class, 'Car':
bmw = Car('BMW', 'Series 3')
print(bmw.make) # BMW
print(bmw.model) # Series 3
print(bmw.noOfCylinders)
bmw.start()
bmw.make = "Audi"
bmw.model = "Series 4"


toyota = Car('Toyota', 'Camry')
print(toyota.make)
print(toyota.model)
toyota.start()

landRover = Car("Land Rover", "LR3")
print(landRover.make)
print(landRover.honk())
print(landRover.turn('left'))

print("------------------------")

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def run(self):
        print(self.name + " is running.")

    def walk(self):
        print(self.name + " is walking")

class Cheetah(Animal):
    # Parent class inheritance
    def __init__(self):
        # parents constructor (initializer):
        super(Cheetah, self), __init__('Cheetah', 'Cats')
        self.name = ""




        
