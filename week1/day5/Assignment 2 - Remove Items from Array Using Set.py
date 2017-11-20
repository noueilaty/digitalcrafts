# Now that you have completed the previous assignment in which you removed the items in the array using for loop now recreate the same app using sets. This will require bit of a research of how sets work in Python.
#
#
#
# Given an array:
#
# names = ["Alex","Mary","Steve","John","Seinfeld","Alan","Jane"]
#
# Write an app using sets which removes the following names from the above array:
#
# namesToRemove = ["Steve","Alan"]
#
# In the end names array will look like this:
#
# names = ["Alex","Mary","John","Seinfeld","Jane"]

names = ["Alex", "Mary", "Steve", "John", "Seinfeld", "Alan", "Jane"]
namesToRemove = ["Steve","Alan"]

def remove_names(arr, remove_arr):
    for name in remove_arr:
        arr.remove(name)
    return arr

print(remove_names(names, namesToRemove))
