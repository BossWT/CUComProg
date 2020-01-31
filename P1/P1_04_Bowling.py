s = input()
n = int(input())
score = [0]
total = 0
frame = 1
count = 0
for i in range(0, len(s)):
    if frame == 10:
        score.append(s[i:])
        break
    if s[i] == 'X':
        count = 0
        score.append(s[i] + s[i + 1] + s[i + 2])
        frame += 1
    elif s[i] == '/':
        count = 0
        score.append(s[i - 1] + s[i] + s[i + 1])
        frame += 1
    else:
        count += 1
        if count == 2:
            score.append(int(s[i - 1]) + int(s[i]))
            frame += 1
            count = 0
for i in range(1, 11):
    temp = 0
    if(type(score[i]) == str):
        for j in range(0, len(score[i])):
            if score[i][j] == 'X':
                point = 10
            elif score[i][j] == '/':
                point = 10 - int(score[i][j - 1])
            else:
                point = int(score[i][j])
            temp += point
        score[i] = temp
    total += score[i]
if(n >= 1 and n <= 10):
    print(score[n])
else:
    print(total)
