try:
    print(x)
except Exception as e:
    print('An exception occurred:', e)
else:
    print('Exception else')
finally:
    print('Finally called')

print('======================')


class ValidationError(Exception):
    def __init__(self, i, errors):
        super().__init__(i)
        self.i = i


def method_with_exception(i):
    if not isinstance(i, int):
        raise ValueError('variable i must be integer')
    elif i < 10:
        raise ValidationError('Validation error, i  must be less than 5', i)
    else:
        return i + 10


try:
    print(method_with_exception('s'))
except ValueError as e:
    print('An exception occurred:', e)

try:
    print(method_with_exception(5))
except ValidationError as e:
    print('An exception occurred:', e)

try:
    print('Result value', method_with_exception(10))
except ValueError as e:
    print('An exception occurred:', e)


