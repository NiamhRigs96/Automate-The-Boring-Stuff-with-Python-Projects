#!/usr/bin/env python3


# Empty list
catNames = []

# While loop
while True:
    # Ask for input of cat name; str(len(catNames) + 1) is eg. CAT 1
    name = input('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    print(name)
    
    # If no name then the code breaks and no more names added
    if name == '':
        break
    
    # List concatenation - Joining catNames with name
    catNames = catNames + [name] 


print('The cat names are: ')

for name in catNames:
    print('    ' + name)
    