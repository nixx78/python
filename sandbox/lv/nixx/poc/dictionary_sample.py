currencies = [{'curr': 'EUR', 'rate': 1},
              {'curr': 'USD', 'rate': 1.14},
              {'curr': 'UAH', 'rate': 32}]

print(currencies)

print(list(map(lambda x: x['curr'], currencies)))

# Take element from current field
print(currencies[0]['curr'])

list_a = [1, 2, 3, 10]
list_b = [10, 20, 30]

print(list(map(lambda x, y: x + y, list_a, list_b)))

dictionary = dict({'EUR': {'curr': 'EUR', 'rate': 1},
                   'USD': {'curr': 'USD', 'rate': 1.14}})

print('Value from dictionary: ' + str(dictionary['EUR']))
print('\'EUR\' in dictionary: ' + str('EUR' in dictionary))
print('\'ABC\' in dictionary: ' + str('ABC' in dictionary))

# Convert plain collection to dict
currMap = {}
for c in currencies:
    currMap[c['curr']] = c

print('All values: ' + str(currMap))
