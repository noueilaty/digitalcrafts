# Given an list of numbers, print each number in the list that is even.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def find_even_numbers(nums):
    even_numbers = []

    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print(find_even_numbers(numbers))
