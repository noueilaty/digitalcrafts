# Calculate the factorial for the user inputed number.

print("Enter a number to calculate its factorial")
user_number = int(raw_input("> "))

def calculate_factorial(num):
    if num != 0:
        factorial = 1
        for index in range(1, num + 1):
            factorial *= index
        return factorial
    else:
        return 0

print(calculate_factorial(user_number))
