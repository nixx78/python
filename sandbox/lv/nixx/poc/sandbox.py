from lv.nixx.poc.domain.classes import *

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

print('-------------------')
lst = ['one', 'two', 'three']
for p, c in enumerate(lst):
    print(p, ':', c)

lst = ['1', '2', '3', '4', '5']
if 'X' in lst:
    print('exists, lenght', len(lst))
else:
    print('not exists , lenght', len(lst))

# Union & update sample
colors = {'red', 'blue', 'orange'}
colors = colors.union({'red', 'blue', 'green'})
colors.update({'white', 'black'})
print(colors)

print('difference', colors.difference({'yellow', 'dark blue', 'red'})) # without red
print('difference', {'yellow', 'dark blue', 'red'}.difference(colors))

