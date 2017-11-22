num1 = input('Enter the first number > ')
num2 = input('Enter the second number > ')
operator = input('Enter the operator > ')

class Calculator(object):

    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2
