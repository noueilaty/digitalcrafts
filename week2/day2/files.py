filename = 'helloworld.txt'
;
# reading the whole file at once
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# reading the file line by line:
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
    for line in lines:
        print(line.rstrip('\n'))

# writing a file: 'w' to write:
with open('fileToWrite.txt', 'w') as file_object:
    file_object.write('Hello World. I am using Python to write a file')

# appending file: 'a' to append:
with open('appendintToFile.txt', 'a') as file_object:
    file_object.write('Hello World')
    file_object.write('\n')
