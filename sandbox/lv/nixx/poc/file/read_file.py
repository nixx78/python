rFile = open('../../../sample.file', 'r+')

lines = rFile.readlines()

sum = 0

for n in range(0, len(lines)):
    if n == 1:
        print('!!!')
    s = lines[n]
    print(n, '#', s)
    sum = sum + int(s)

print('complete, sum', sum)

rFile.write('\n')
rFile.write('Sum:' + str(sum))
rFile.close()
