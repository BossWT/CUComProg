n = input()
a = n[3::7]
b = n[7::5]
let = ['-','A','B','C','D','E','F','G','H','I','J']
sum = int(a)+int(b)+10000
sum = str(sum)
code = sum[-4:-1]
# print(a)
# print(b)
# print(sum)
# print(code)
sum = 0
for c in code:
    sum += int(c)
sum = str(sum)
index = int(sum[-1])+1
# print(sum)
# print(index)
print(code+""+let[int(index)])