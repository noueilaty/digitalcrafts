# You are responsible for creating an app that manages groceries. Your groceries are characterized by Shopping Lists which can contain grocery items. Here are the features you need to implement:
#
# * You don't need to ask the user for the input. Simply create the classes with the corresponding relationships and test it out by creating instances of the class.
#
# - A user should be able to create a shopping list. A shopping list consists of a title and description. Example = Fiesta, Walmart, Sams Club, Cosco, Randalls etc
#
# - A user should be able to add a grocery items to a particular shopping list. A grocery item consists of a title. Example Milk, Cookies, Paper, Napkins, Soda, Chips etc
#
# - A user should be able to add multiple shoppings lists
#
#
#
# * Add at least 5 items in 3-5 shopping lists and then print the shopping list along with the grocery items as shown below:
#
# Fiesta
# Milk, Soda, Fish
#
# Walmart
# Paper, Napkins, Plate, Chips
#
# Sams Club
# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey



class Shopping_list(object):
    def __init__(self, title):
        self.title = title
        self.groceries = []

    def add_grocery(self, item):
        self.groceries.append(item)

fiesta = Shopping_list('Fiesta')
fiesta.add_grocery('Milk')
fiesta.add_grocery('Soda')
fiesta.add_grocery('Fish')

print(fiesta.groceries)

walmart = Shopping_list('walmart')
walmart.add_grocery('Paper')
walmart.add_grocery('Napkins')
walmart.add_grocery('Plate')
walmart.add_grocery('Chips')

print(walmart.groceries)

sams_club = Shopping_list('Sams Club')
sams_club.add_grocery('Chicken')
sams_club.add_grocery('Beef')
sams_club.add_grocery('Eggs')
sams_club.add_grocery('Sugar')
sams_club.add_grocery('Salt')
sams_club.add_grocery('Pepper')
sams_club.add_grocery('Honey')
