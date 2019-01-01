import csv
from datetime import datetime
from itertools import groupby

txns = []

with open('txn.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        txn = dict()
        txn['id'] = row['id']
        txn['currency'] = row['currency']
        txn['date'] = datetime.strptime(row['date'], '%m/%d/%Y')
        txn['amount'] = float(row['amount'])
        txn['accountId'] = row['account_id']
        txns.append(txn)

for account, accountGroup in groupby(txns, lambda x: x['accountId']):
    print('Account: ', account)
    for currency, currencyGroup in groupby(accountGroup, lambda x: x['currency']):
        currs = list(currencyGroup)
        print('\t\tCurrency:', currency)
        for c in currs:
            print('\t\t\tid:', c['id'], 'date: ', c['date'].strftime('%m/%d/%Y'), c['amount'])
