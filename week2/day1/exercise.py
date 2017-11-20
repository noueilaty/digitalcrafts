class Restaurant:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.itemsOrdered = 0

    def print_description(self):
        print(self.title + ',' + self.description)

    def orderItem(self):
        self.itemsOrdered += 1

    def displayOrderStatus(self):
        print('We ordered ' + str(self.itemsOrdered) + ' items.')

georges = Restaurant("George's Pastaria", "Classic homemade italian cuisine")

georges.print_description()
georges.orderItem()
georges.orderItem()
georges.displayOrderStatus()
