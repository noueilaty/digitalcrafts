# Ask the user the temperature in Celcius

# temp_celcius = raw_input("Enter temperature in celcius > ")
#
# print("You entered {}".format(temp_celcius))
#
# # To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
# temp_to_farenheit = (int(temp_celcius) * 1.8 + 32)
#
# print("{0} degrees Celcius converted to Farenheit is {1} degrees".format(temp_celcius, temp_to_farenheit))


############################
# def convert_celcius_to_farenheit(celcius):
#     farenheit = celcius * 1.8 + 32
#     print("You entered {} degrees celcius.".format(celcius))
#     print("{0} degrees Celcius is {1} degrees Farenheit.".format(celcius, farenheit))

import temperature_helper as t

celcius = int(raw_input("Enter temperature in celcius > "))

t.convert_celcius_to_farenheit(celcius)
# convert_celcius_to_farenheit(celcius)

# modules - Separating code into files for resuability.
