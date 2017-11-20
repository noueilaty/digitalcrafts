# Create an app which takes two numbers as input from the user and then prints out the results of addition on the screen.

number1 = int(raw_input("Enter a number >   "))
number2 = int(raw_input("Enter another number >   "))
total = number1 + number2

print("{0} and {1} equal {2}".format(number1,number2,total))
