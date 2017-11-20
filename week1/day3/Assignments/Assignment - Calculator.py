# In this assignment you are going to build a calculator. You are going to take three inputs from the user.
#
#
#
# Input 1 - Represents the first number
#
# Input 2 - Represents the operand (+, - , * , /)
#
# Input 3 - Represents the second number
#
# Based on the operand you are going to perform the math operation and print the result on the terminal.
#
# - Make sure each math operation is a separate function.

###########
# Completed
###########

import calculator_helper

first_number = raw_input("Enter the first number > ")
operand = raw_input("Enter the operand you'd like to use (+, - , * , /) > ")
second_number = raw_input("Enter the second number > ")

calculator_helper.calculate(first_number, operand, second_number)
