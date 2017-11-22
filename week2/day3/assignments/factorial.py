class Factorial(object):

    def __init__(self):
        pass

    def factorial(self, num):
        if num != 0:
            factorial = 1
            for index in range(1, num + 1):
                factorial *= index
            return factorial
        else:
            return 0
