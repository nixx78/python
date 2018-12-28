from lv.nixx.poc.domain.classes import *

s = list('9123945678')

s.append('0')
s.sort()

print(s)

x = lambda a, b: a + b
print(x(5, 11))

p1 = Person('1', 'Name.Value', 'Surname.Value')
print(p1.surname)

del p1.surname

try:
    s = p1.surname
except: AttributeError
print('Attribute not exists')

if not hasattr(p1, 'surname'):
    print('No attribute')
