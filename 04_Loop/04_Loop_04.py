str = input()
ans = ''
for s in str:
    if s == '(':
        s = '['
    elif s == '[':
        s = '('
    elif s == ')':
        s = ']'
    elif s == ']':
        s = ')'
    ans += s
print(ans)
