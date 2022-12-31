import os
# myfile = open("/home/sunil/Desktop/Sunil/Python/sunil.txt")
# myfile = open('test.txt')
# this will through error as here is no file
with open('sunil.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('sunil.txt',mode='r') as myfile:
    #r - read file, a - append file, w- write or over write only , r+ reading and writing, w+ writing and reading
    contents = myfile.read()
    print(contents)

#append file
with open('sunil.txt',mode='a') as myfile:
    myfile.write('Marella')

#write file. if file not exist, it creates the file
with open('sunil.txt',mode='w') as myfile:
    myfile.write('Marella')

