dna = input().strip()
op = input()
dna = dna.upper()
base = ['A', 'T', 'G', 'C']
pairs = ['T', 'A', 'C', 'G']
amount = [0, 0, 0, 0]
for i in dna:
    if i not in base:
        print('Invalid DNA')
        exit()
if op == 'R':
    res = ''
    for i in dna:
        res += pairs[base.index(i)]
    res = res[::-1]
    print(res)
elif op == 'F':
    for i in dna:
        amount[base.index(i)] += 1
    print('A=' + str(amount[0]) + ', ' + 'T=' + str(amount[1]) +
          ', ' + 'G=' + str(amount[2]) + ', ' + 'C=' + str(amount[3]))
elif op == 'D':
    pair = input()
    n = 0
    for i in range(len(dna) - 1):
        check = dna[i] + dna[i + 1]
        if check == pair:
            n += 1
    print(n)
