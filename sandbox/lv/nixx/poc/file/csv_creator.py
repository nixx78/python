import csv

with open('sample.out.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=':', quotechar='\'', quoting=csv.QUOTE_NONNUMERIC)
    csvWriter.writerow(['column1', 'column2', 'column3'])

    for i in range(1, 5):
        row = []
        for c in ['A', 'B', 'C']:
            row.append(str(i) + c)
        csvWriter.writerow(row)


