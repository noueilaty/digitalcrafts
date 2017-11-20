# arrays
names = ['Alex', 'John', 'Mary', 'Steve', 'Hassan']


# loops
for index in range(0,len(names)):
    print(names[index])

# Create an array of whole numbers and print the double of those numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for index in range(0,len(numbers)):
    print(numbers[index] * 2)


# forEach loop
# Goes through all the items from first to last. Cannot be run backwards.
for name in names:
    print(name)

# appending the items to the array (adding)
names.append('Jeff')

print(names)
# returns:
# Traceback (most recent call last):
#   File "w1d4_notes.py", line 22, in <module>
#     names.append('Jeff')
# AttributeError: 'str' object has no attribute 'append'

del names[1]

print(names)

# inserting at particular position
names.insert(4, "Stephen")

print(names)

print("-------------------------")

print("Enter name to delete")
name_to_delete = raw_input("> ")

print("Searching for '{}'".format(name_to_delete))

#This won't work since 'name' is a copy of the original name. So when it deletes the name it's only deleting the copy, not the original inside the array.
# for name in names:
#     if name == name_to_delete:
#         print("Deleting {}".format(name_to_delete))
#         del name
#         print("Deleted")
#         break
#     else:
#         print("{} not found".format(name_to_delete))
#
# print("Updated array: {}".format(names))



for index in range(0,len(names)):
    if names[index] == name_to_delete:
        print("Deleting {}".format(name_to_delete))
        del names[index]
        print("Deleted")
        break
    else:
        print("{} not found.".format(name_to_delete))

print("Updated array: {}".format(names))

# To search within an array:
