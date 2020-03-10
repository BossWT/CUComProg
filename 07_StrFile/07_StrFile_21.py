sen = []
ans = []
str = input()
sen.append(str)
while True:
    str = input()
    if str != 'end':
        sen.append(str)
    else:
        break
for i in sen:
    str = ''
    for j in i:
        shift = ''
        if j.isalpha():
            if j.isupper():
                shift = chr((((ord(j) - 65) + 13) % 26) + 65)
            else:
                shift = chr((((ord(j) - 97) + 13) % 26) + 97)
        else:
            shift = j
        str += shift
    ans.append(str)
for x in ans:
    print(x)
