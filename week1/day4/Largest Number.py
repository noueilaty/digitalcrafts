# Given an list of numbers, print the largest of the numbers.

numbers = [1, 2, 3, 5, 6, 11, 1, 4]

def find_largest_number(nums):
    largest_number = 0

    for num in nums:
        if num > largest_number:
            largest_number = num
    return largest_number

print(find_largest_number(numbers))
