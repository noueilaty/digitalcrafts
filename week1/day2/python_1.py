name = raw_input("What is your name?")
age = raw_input("What is your age?")
address = "1200 Richmond Ave"

# message = name + age
#
# print(name)
# print(age)

# String interpolation:
message = "My name is {0} and my age is {1} and my address is {2}.".format(name,age,address)

print(message)
