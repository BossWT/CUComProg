n = int(input())
d_contact = {}
rd_contact = {}
for i in range(n):
    first, last, tel = input().split()
    name = first + ' ' + last
    d_contact[name] = tel
    rd_contact[tel] = name
m = int(input())
for i in range(m):
    key = input()
    ans = ''
    if key in d_contact:
        print(key, '-->', d_contact[key])
    elif key in rd_contact:
        print(key, '-->', rd_contact[key])
    else:
        print(key, '-->', 'Not found')
