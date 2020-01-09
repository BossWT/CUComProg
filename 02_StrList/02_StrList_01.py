id = input()
digit = 13
sum = 0
for n in range(0,12):
    sum+=digit*int(id[n])
    digit-=1
last = sum%11
last = 11-last
last = last%10
i=1
for n in id:
    print(n,end="")
    if i==1 or i== 5 or i==10 or i==12:
        print(" ",end="")
    i+=1
print(last)