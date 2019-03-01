from lv.nixx.poc.domain.classes import *
from datetime import datetime

s = list('9123945678')

s.append('0')
s.sort()

print(s)

x = lambda a, b: a + b
print(x(5, 11))

p1 = Person(1, 'Name.Value', 'Surname.Value')
print(p1.surname)

del p1.surname

try:
    s = p1.surname
except:
    AttributeError
print('Attribute not exists')

if not hasattr(p1, 'surname'):
    print('No attribute')

print('-------------------')

print(list(range(1, 10, 2)))

print('-------------------')

for i in range(3):
    print(i)

print('-------------------')
i = 0
while i < 5:
    print(i)
    i = i + 1

print('-------------------')
i = 0
while i < 5:
    if i == 2:
        break
    else:
        i = i + 1
    print(i)

print('-------------------')
print(i)

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if i == 3:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")

print('-------------------')
for i in range(3):
    print(i)
    if i == 2:
        break
else:
    print('else')


print('-------------------------------')
d = datetime.now()
print('Date, now:', d)
print('This year is:', d.year)
print('Today is:', d.strftime("%A"))

print('Constructed date:', datetime(2019, 3, 1))
print('Constructed date with time:', datetime(2019, 3, 1, 13, 1, 52))

print('Formatted date:', datetime(2019, 3, 1, 13, 1, 52).strftime("%c"))
print('Created from string:', datetime.strptime('01/03/2019 14:59:01', '%d/%m/%Y %H:%M:%S'))


