sol = input()
ans = input()
mark = 0
for a, b in zip(sol, ans):
    if a == b:
        mark += 1
if len(sol) != len(ans):
    print('Incomplete answer')
else:
    print(mark)
