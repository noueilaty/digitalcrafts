# Write a Fizz Buzz application.
#
# Take input from the user. If the input is divisible by 3 then print "Fizz", if the input it divisible by 5 then print "Buzz". If the input is divisible by 3 and 5 then print "Fizz Buzz".

###########
# Completed
###########

user_input = int(raw_input('Enter any number to determine if it\'s a Fizz, Buzz, or FizzBuzz > '))

if user_input % 3 == 0 and user_input % 5 == 0:
    print('FizzBuzz')
elif user_input % 3 == 0:
    print('Fizz')
elif user_input % 5 == 0:
    print('Buzz')
else:
    print('{} is not divisible by 3 nor 5'.format(user_input))
