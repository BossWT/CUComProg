n = int(input())
step = []
while n != 1:
    step.append(n)
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
if len(step) > 15:
    for i in range(len(step) - 14, len(step)):
        print(step[i], end='->')
    print('1')
else:
    for i in range(len(step)):
        print(step[i], end='->')
    print('1')
