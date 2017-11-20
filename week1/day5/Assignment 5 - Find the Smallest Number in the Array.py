# Given an array:
#
# [2,3,45,12,234,5,6,789]
#
# Write an app which finds the smallest number in the array.

numbers = [99,3,45,12,234,5,6,789]

def find_smallest_number(numsArr):
    smallest_number = numsArr[0];
    for num in numsArr:
        if num < smallest_number:
            smallest_number = num

    return smallest_number

print(find_smallest_number(numbers))
