s = lambda a, b: a + b

print(s(1, 2))


def mapper(a): return a + 'mapped'

lst = ['1', '2', '3', '4', '5']

mappedLst = map(mapper, lst)
print('Mapped list:', ' '.join(mappedLst))
