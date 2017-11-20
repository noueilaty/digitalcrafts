# Update your Calculator app to repeatedly ask the user to input the following:
#
# - Input first number
#
# - Input operand
#
# - Input second number
#
# If the operand is not "+" or +"-" or "*" or "/" then print a message to input correct operand.
#
# If the input is not a number than tell the user that they need to input numbers only.
#
# The user can quit the app by pressing "q"

def calculate(num1, oper, num2):
    print(eval('{0} {1} {2}'.format(num1, oper, num2)))


while True:
    try:
        user_num1 = raw_input('Enter the first number you\'d like to calculate > ')
        user_oper = raw_input('Enter the operator for your calculation > ')
        user_num2 = raw_input('Enter the second number you\'d like to calculate > ')

        if user_oper not in ["+", "-", "*", "/"]:
            print('{} is an invalid operator'.format(user_oper))
        else:
            calculate(user_num1, user_oper, user_num2)

    except:
        print("Error: Must enter an integer")

    choice = raw_input("Press q to quit \nPress any other key to continue\n> ")
    if choice == "q":
        break
