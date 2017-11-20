# # Given an array:
# names = ["Alex","Mary","Steve","John","Seinfeld","Alan","Jane"]
#
# Write an app which removes the following names from the above array:
# namesToRemove = ["Steve","Alan"]
#
# In the end names array will look like this:
# names = ["Alex","Mary","John","Seinfeld","Jane"]

names = ["Alex", "Mary", "Steve", "John", "Seinfeld", "Alan", "Jane"]
namesToRemove=["Alan", "Steve"]

indexToDelete = -1

for nameR in namesToRemove:
    for index in range(0, len(names)):
        if nameR == names[index]:
            indexToDelete = index

    del names[indexToDelete]

print(names)
