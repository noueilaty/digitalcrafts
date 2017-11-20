###########
# functions
###########
def greet(name):
    print("Hello {}".format(name))

print("Outside the function")

greet("Hassan")


# Not common but something to consider:
def getAirport():
    return "IAH" 2345

(name, code) = getAirport()
print(name)
print(code)

#########################
# Setting a default value
#########################
def create_pizza(name = 'Cheese Pizza', email = '', coupon_code = '')
    print(name)

# default value is run:
print(create_pizza())

# ignores default value, and passed value is run:
print(create_pizza("Pepperoni Pizza"))

# name the arguments that define what you're doing:
create_pizza(name = "Chicken Pizza", email = "johndoe@gmail.com")


# If number of parameters is unknown:
def add_toppings(*toppings):
    print(toppings)

# returned value is an array:
add_toppings('Mushroom', 'Tomato', 'Cheese', 'Green Pepper')
