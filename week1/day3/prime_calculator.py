input_num = input("Enter a number to check if it's prime or not > ")

def isPrime(num):
    # If the number is divisible by ONLY 'itself AND 1', it's a prime number. Otherwise, it's not a prime number.
    captured_numbers = []

    for p in range(2, num + 1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            captured_numbers.append(p)
    print(captured_numbers)

isPrime(int(input_num))
