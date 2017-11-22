# Check to see if user inputed word is a palindrome.
# Not allowed to use any reverse string methods.

# Ask user for input
# lowercase the input, then loop through the string, checking to see if each character matches

backwards_word = []

def reverseWord(word):
    for char in word:
        backwards_word.insert(0, char)
        # print(backwards_word)
    return ''.join(backwards_word)


print("Enter a word to check if it is a palindrome")
user_word = str.lower(raw_input("> "))


if reverseWord(user_word) == user_word:
    print("{} is a palindrome!".format(user_word))
else:
    print("{} is not a palindrome!".format(user_word))
