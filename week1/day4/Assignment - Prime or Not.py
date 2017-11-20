# A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself

def prime_calculator(num):
    divisors = []
    for index in range(1, num + 1):
        if num % index == 0:
            divisors.append(index)
            print(divisors)
    if (len(divisors) > 2):
        print("{} is not a prime number.".format(num))
    else:
        print("{} is a prime number.".format(num))

print("Enter a number to determine if it's a prime:")
user_number = int(raw_input("> "))

prime_calculator(user_number)
