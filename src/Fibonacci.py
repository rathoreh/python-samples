'''
Created on 18 Mar 2019

@author: me
'''

n = int(input("Enter limit: "))
a, b = 0, 1
while a <= 10:
    print(a, end=' ')
    a,b = b, a+b

print('\n')

a, b = 0, 1
while a <= n:
    print(a)
    a,b = b, a+b
