'''
Created on 11 Mar 2019

@author: me
'''

my_list = [1,4,9,16,25]
print(my_list)

my_list = my_list + [36,49]
print(my_list)
print()

print(my_list[3])
print(my_list[-3])
print()

print(my_list[0:3])
print()

cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)
print()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print()

letters[2:5] = ['C', 'D', 'E']
print(letters)
print()

letters[2:5] = []
print(letters)
print()

letters[:] = []
print(letters)
print()
