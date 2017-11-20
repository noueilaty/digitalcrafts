def calculate(num1, oper, num2):
    print(eval('{0} {1} {2}'.format(num1, oper, num2)))

user_num1 = raw_input(print("Enter the first number you'd like to calculate > "))
user_oper = raw_input(print("Enter the operator for your calculation > "))
user_num2 = raw_input(print("Enter the second number you'd like to calculate > "))
