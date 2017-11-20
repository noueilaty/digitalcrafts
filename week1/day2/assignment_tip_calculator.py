# In this assignment you are going to ask the user for the two inputs as shown below:
#
# - Enter the total amount
#
# - Enter the tip percentage amount
#
# After the user has entered both inputs the application calculates the tip amount and displays it to the user.

total_amount = raw_input("What is your bill total?")
tip_percentage = raw_input("What is the tip percentage you'd like to leave?")

calculate_tip_amount = float(total_amount) * float(tip_percentage)

print("The tip amount is: ${0}".format(str(calculate_tip_amount)[:4]))
 
