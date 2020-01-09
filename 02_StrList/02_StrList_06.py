a = input()
b = input()
u=[]
v=[]
ans=[]
num = ''
sum = 0
for i in range(1,len(a)):
    if a[i] != ',' and a[i] !=']':
        num+=a[i]
    else:
        u.append(float(num))
        num=''
for i in range(1,len(b)):
    if b[i] != ',' and b[i] !=']':
        num+=b[i]
    else:
        v.append(float(num))
        num=''
ans.append(u[0]+v[0])
ans.append(u[1]+v[1])
ans.append(u[2]+v[2])
print(u,end=" + ")
print(v,end=" = ")
print(ans)