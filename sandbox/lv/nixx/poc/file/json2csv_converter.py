import json
import csv

with open('txn_tree.json', 'r') as json_file:
    json_str = json_file.read()

json1_data = json.loads(json_str)

out_list = []

for a in json1_data:
    account = a['account']
    curr = a['currency']
    row = {}
    for t in a['txns']:
        row = {'id': int(t['id']), 'account': account, 'currency': curr, 'amount': t['amount'], 'date': t['date']}

    out_list.append(row)

out_list = sorted(out_list, key=lambda t1: t1['id'])

keys = out_list[0].keys()

csv.register_dialect('customDialect', delimiter=':', quoting=csv.QUOTE_NONNUMERIC, quotechar='\'', escapechar='\\')

with open('txns.out.csv', newline='', encoding='UTF-8', mode='w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, dialect='customDialect')
    dict_writer.writeheader()
    dict_writer.writerows(out_list)
