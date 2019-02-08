def method_concat(a: int, s='default'):
    return str(a) + s


print(method_concat(5, 'string'))
print(method_concat(s='abs', a=5))
print(method_concat(5))
print(method_concat(a=10))


def sumWithVarArgs(*varargs: int):
    return sum(varargs)


print('Sum:', sumWithVarArgs(1, 2, 3, 4, 5))


def sumWithVarArgs(*varargs: str):
    s = ''
    for n in varargs:
        s = s + n
    return s


print('Sum:', sumWithVarArgs('1', '2', '3', '4', '5'))