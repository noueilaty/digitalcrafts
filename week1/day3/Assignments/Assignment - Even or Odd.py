# Write an app which ask user for an input and then displays a message indicating whether the number is even or odd.

###########
# Completed
###########

number_given = int(raw_input('Enter a number to determine if a number is even or odd > '))

if number_given % 2 == 1:
    print('{} is an odd number'.format(number_given))
else:
    print('{} is an even number'.format(number_given))
