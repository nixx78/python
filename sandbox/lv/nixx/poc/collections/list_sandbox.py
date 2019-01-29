# List is a collection which is ordered and changeable. Allows duplicate members.

from lv.nixx.poc.domain.classes import Person

lst = ['one', 'two', 'three']
for p, c in enumerate(lst):
    print(p, ':', c)

print('-------------------')
lst = ['1', '2', '3', '4', '5']
if 'X' in lst:
    print('exists, lenght', len(lst))
else:
    print('not exists , lenght', len(lst))

print('-------------------')

# Union & update sample
colors = ['red', 'blue']
colors.insert(1, 'black')
colors.append('orange')
colors.sort()

print(colors)

print('index of blue', colors.index('blue'))

print('-------------------')
persons = [
    Person(3, 'name3', 'surname3'),
    Person(1, 'name1', 'surname1'),
    Person(4, 'name4', 'surname4'),
    Person(2, 'name2', 'surname2')
]
persons.sort(reverse=True, key=lambda pers: pers.name)
print(persons)

persons.sort()
print(persons)
