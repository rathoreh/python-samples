'''
Created on 6 Mar 2019

@author: me
'''

print('C:\some\name')

print(r'C:\some\name')

print(3 * 'Hey' + '!Yo')

print('Py' 'thon' ' 3.7.2')

prefix = 'Py'
# prefix 'thon' <<< No no, not allowed; only works with literals
print(prefix + 'thon' + ' 3.7.2')

text = ('Put several strings within parentheses '
         'to have them joined together.')
print(text)

text = 'Python'
print(text[0])
print(text[3])
print(text[-1])
print(text[-6:-1])
#print(text[10]) -- string index out of range
print(text[1:4])
print(text[3:])
print(text[:2])
print(text[-2:])

print(text)
text = 'J' + text[1:]
print(text)

print(len(text))