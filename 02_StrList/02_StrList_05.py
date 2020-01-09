str = input()
num = ''
sum=0
l = len(str)
i=1
for s in str:
    # print(i)
    if s!=' ':
        num+=s
    else:
        # print(num)
        if num=='':
            num=0
        sum+=int(num)
        num = ''
    if i==l:
        sum+=int(num)
    i+=1
print(sum)