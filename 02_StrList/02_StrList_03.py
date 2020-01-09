str = input()
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
ch = ''
day = ''
mon = ''
i=0
for s in str:
    if s!='/':
        ch+=s
    else:
        if i==0:
            day=ch
            ch=''
            i+=1
        elif i==1:
            mon=ch
            ch=''
            i+=1
year = str[-4:]
print(month[int(mon)-1],end=" ")
print(day,end=", ")
print(year)