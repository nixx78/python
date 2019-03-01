# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values

person = {
    'id': '10001',
    'name': 'John',
    'surname': 'Rambo',
    'dateOfBirth': '06/12/1978'
}
print('Person dictionary: ', person)

print('Dictionary person items:')
for key, value in person.items():
    print('Key [', key, '] Value [', value, ']')

person['name'] = 'Name.Updated'
print('Updated name:', person['name'])

del person['dateOfBirth']
print('Person dictionary with deleted "dateOfBirth":', person)

person = dict(id='1', name='John', surname='Rambo', dateOfBirth='06/12/1978')
print('Person dictionary: ', person)

print('Setdefault (not exists):', person.setdefault('notExistingKey', 'defaultValue'))
print('Setdefault (exists)', person.setdefault('name', 'defaultValue'))

currencies = [{'curr': 'EUR', 'rate': 1},
              {'curr': 'USD', 'rate': 1.14},
              {'curr': 'USD', 'rate': 2.56},
              {'curr': 'UAH', 'rate': 32}]

print(currencies)

print('Unique currencies:', set(map(lambda x: x['curr'], currencies)))

# Take element from current field
print(currencies[0]['curr'])

list_a = [1, 2, 3, 10]
list_b = [10, 20, 30]

print(list(map(lambda x, y: x + y, list_a, list_b)))

dictionary = dict({'EUR': {'curr': 'EUR', 'rate': 1},
                   'USD': {'curr': 'USD', 'rate': 1.14}})

print('Value from dictionary: [] ', str(dictionary['EUR']))
print('Value from dictionary: get: ', dictionary.get('EUR'))

print('\'EUR\' in dictionary: ', 'EUR' in dictionary)
print('\'ABC\' in dictionary: ', 'ABC' in dictionary)

# Convert plain collection to dict
currMap = {}
for c in currencies:
    currMap[c['curr']] = c

print('All values: ', currMap)
