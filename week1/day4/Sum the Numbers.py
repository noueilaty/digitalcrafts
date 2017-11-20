# Sum the Numbers
# Given a list of numbers, print their sum. When I say given something, just make something up and store it in a variable.

numbers = [5, 6, 8, 7, 3, 1, 2]

def sum_numbers(nums):
    sum_of_numbers = 0

    for num in nums:
        sum_of_numbers += num
    return sum_of_numbers

print(sum_numbers(numbers))
