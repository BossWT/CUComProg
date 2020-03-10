st = input()
st = st.lower()
str = ''
for i in st:
    if i.isalnum():
        str += i
    else:
        str += ' '
str = str.strip()
str = str.split()
ans = str[0]
for i in range(1, len(str)):
    str[i] = str[i][0].upper() + str[i][1:]
    ans += str[i]
print(ans)
