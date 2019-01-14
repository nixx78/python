import csv
import json
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

report = []

for account, accountGroup in groupby(txns, lambda x: x['accountId']):
    for currency, currencyGroup in groupby(accountGroup, lambda x: x['currency']):
        accTxns = []
        for c in currencyGroup:
            accTxns.append({'id': c['id'], 'date': c['date'].strftime('%m/%d/%Y'), 'amount': c['amount']})

        report.append({'account': account, 'currency': currency, 'txns': accTxns})

json = json.dumps(report, sort_keys=True, indent=4)
print(json)

outFile = open('report.out.json', "w")
outFile.write(json)
