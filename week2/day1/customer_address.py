class Address:
    def __init__(self, streetName, state, zipcode):
        self.street = ""
        self.state = ""
        self.zipcode = ""

class Customer:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.addresses = []


customer = Customer()
customer.firstName = "John"
customer.lastName = "Doe"

address1 = Address("1200 Richmond Ave", "TX", "77042")
address2 = Address("3200 Harvin Ave", "TX", "77098")

customer.addresses.append(address1)
customer.addresses.append(address2)


print(customer.firstName + " " + customer.lastName)




class Job:
    def __init__(self):
        self.title = ""
        self.location = ""
        self.department = ""

class Employee(object):
    def __init__(self, firstName, lastName):
        #self.firstName is visible anywhere inside the class
        self.firstName = firstName
        self.lastName = lastName
        self.job = Job()

employee = Employee("John", "Doe")
employee.job = Job()

employee.job.title = "Mechanic"
employee.job.location = "Houston"
employee.job.department = "IT"

print(employee.firstName + " " + employee.lastName)
print(employee.job.title + " " + employee.job.location)
