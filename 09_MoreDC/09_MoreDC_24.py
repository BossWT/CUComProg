from collections import OrderedDict
d = OrderedDict()
while True:
    line = input()
    if line == 'q':
        break
    data = line.split(', ')
    if data[1] not in d:
        d[data[1]] = [data[0]]
    else:
        d[data[1]].append(data[0])
for k, v in d.items():
    print(k + ': ' + ', '.join(v))
