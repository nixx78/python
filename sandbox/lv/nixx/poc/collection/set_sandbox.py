# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

from lv.nixx.poc.domain.classes import Person

colors = {'red', 'blue'}
colors.add('orange')

colors = colors.union({'red', 'blue', 'green'})
colors.update({'white', 'black'})
print('union and updated colors', colors)

print('difference', colors.difference({'yellow', 'dark blue', 'red'}))
print('difference', {'yellow', 'dark blue', 'red'}.difference(colors))

print('intersection: colors.intersection', colors.intersection({'white', 'magenta'}))
print('intersection" colors & {\'white\', \'magenta\'}', colors & {'white', 'magenta'})

intersec = {'red', 'blue', 'green'}
intersec.intersection_update({'yellow', 'dark blue', 'red'}, {'white', 'red', 'magenta'})

print('intersection_update', intersec)

# The symmetric difference of two sets A and B is the set of elements which
# are in either of the sets A or B but not in both.
print('symmetric_difference', colors.symmetric_difference({'black', 'red'}))

colors.symmetric_difference_update({'black', 'red'}) # From colors are removed common element
print('symmetric_difference_update', colors)


persons = {
    Person(3, 'name3', 'surname3'),
    Person(1, 'name1', 'surname1'),
    Person(4, 'name4', 'surname4'),
    Person(2, 'name2', 'surname2')
}

print('persons', {Person(1, 'name1', 'surname1')} & persons)
