print('----------------------------')
# Basics
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.people_greeted = []

    def greet(self, other_person):
        print('Hello {0}, I am {1}'.format(other_person.name, self.name))
        self.greeting_count += 1
        # If the person being greeted is not in the people_greeted list, then add them.
        if other_person not in self.people_greeted:
            self.people_greeted.append(other_person)

    def print_contact_info(self):
        print('{0}\'s email: {1}, {0}\'s phone number: {2}'.format(self.name, self.email, self.phone))

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        friends = 0
        for friend in self.friends:
            friends += 1
        print(friends)

    def __repr__(self):
        print(self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        print("{0} has greeted {1} people.".format(self.name, len(self.people_greeted)))


sonny = Person("Sonny", "sonny@hotmail.com", "483-385-4948")

jordan = Person("Jordan", "jordan@aol.com", "495-586-4356")

Person.greet(sonny, jordan)
Person.greet(jordan, sonny)
print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)

print('----------------------------')
# Make your own class:
class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print('{0} {1} {2}'.format(self.make, self.model, self.year))

car = Vehicle('Nissan', 'Leaf', 2015)
print(car.make, car.model, car.year)

# Add a method
# Add a a print_info() method to the Vehicle class. It will print out the vehicle's information.
car.print_info()

# Add a method 2:
# Go back to the person class. Add a print_contact_info method to the Person class that will print out the contact info for an object instance of Person.
sonny.print_contact_info()

# Add an instance variable (attribute)
jordan.friends.append(sonny)
sonny.friends.append(jordan)

# add an add_friend method:
# added to line 16-17
jordan.add_friend(sonny)

# Add a num_friends method:
jordan.num_friends()

# Count number of greetings:
print(sonny.greeting_count)
sonny.greet(jordan)
sonny.greet(jordan)
print(sonny.greeting_count)

# __repr__
jordan

# Bonus Challenge:
sonny.num_unique_people_greeted()
jordan.num_unique_people_greeted()
