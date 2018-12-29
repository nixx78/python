from lv.nixx.poc.domain.classes import Person

s = lambda a, b: a + b

print(s(1, 2))


def mapper(a): return a + 'mapped'


lst = ['1', '2', '3', '4', '5']

mappedLst = list(map(mapper, lst))
print('Mapped list:', mappedLst)

mappedLst = map(lambda a: a + 'mapped', lst)
print('Mapped list:', ' '.join(mappedLst))

# List of functions
from math import sin, cos, tan, pi


def map_functions(x, functions):
    res = []
    for func in functions:
        res.append(func(x))
    return res


family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))

# filtering
persons = [Person(1, 'Name1', 'Surname1'), Person(2, 'Name2', 'Surname2'), Person(2, 'Name3', 'Surname3')]
filteredPersons = list(filter(lambda p: p.name != 'Name1', persons))

print(filteredPersons)

# reduce
from functools import reduce

print(reduce(lambda x, y: x if x > y else y, (2, 4, 5, 1, 0, 10)))
print(reduce(lambda x, y: x + y, range(1, 101)))
