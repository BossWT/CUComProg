n = int(input())
for i in range(n):
    line = input()
    j = 0
    if line != '':
        while (line[j] == '.'):
            j += 1
        line = line[j:]
    print('.' * int(j / 2), end='')
    print(line)
