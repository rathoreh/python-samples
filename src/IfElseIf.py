'''
Created on 18 Mar 2019

@author: me
'''

try:
    n = int(input('Enter a number: '))

    if n < 0:
        print('You entered a negative number %i' %(n))
    elif n == 0:
        print('You entered zero(0) %i' %(n))
    else:
        print('You entered a positive number %i' %(n))

except ValueError:
    print('Invalid value')
