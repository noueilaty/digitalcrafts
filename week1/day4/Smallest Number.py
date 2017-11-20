# Given an list of numbers, print the smallest of the numbers.

numbers = [9, 3, 5, 21, 3, 1]

def find_smallest_number(nums):
    smallest_number = nums[0]

    for num in nums:
        if num < smallest_number:
            smallest_number = num
    return smallest_number

print(find_smallest_number(numbers))
