# # Given an array:
#
# [2,3,45,12,234,5,6,789]
#
# Write an app which finds the largest number in the array.

numbers = [2, 3, 45, 12, 234, 5, 6, 789]

def find_largest_number(numsArr):
    largest_number = 0

    for num in numsArr:
        if num > largest_number:
            largest_number = num

    return largest_number

print(find_largest_number(numbers))
