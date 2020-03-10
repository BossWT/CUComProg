path, year = input().split()
file = open(path, 'r')
sum = 0
min = 99999
max = -99999
n = 0
for line in file:
    id, score = line.split()
    score = float(score)
    if id[0:2] == year[-2:]:
        n += 1
        sum += score
        if score > max:
            max = score
        if score < min:
            min = score
if n != 0:
    print(min, max, sum / n)
else:
    print('No data')
