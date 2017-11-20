# Enter an app where you will ask the user to input a number between 1 and 100.
#
# User enters: 23
# Take the number and then print out the English language representation of that number. Like
#
# Input: 23
# Output: Twenty Three
#
# Input: 55
# Output: Fifty Five
#
# Input: 19
# Output: Nineteen

user_num = raw_input("Enter a number between 1 and 100 > ")

ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

after_tens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundreds = ['one hundred']

def print_english_representation(num):
    split_num = list(num)
    num = int(num)

    if len(split_num) == 3:
        print(hundreds[0])
    elif len(split_num) == 2:
        if split_num[0] == 1:
            print(after_tens[int(split_num[1]) - 1])
        else:
            print(tens[int(split_num[0]) - 2] + ' ' + ones[int(split_num[1])])
    else:
        print(ones[num])

print_english_representation(user_num)
