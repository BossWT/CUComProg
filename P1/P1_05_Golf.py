import math
sumpar = 0
sumstroke = 0
sumimpstroke = 0
for i in range(9):
    par, stroke, select = input().split()
    stroke = int(stroke)
    par = int(par)
    select = int(select)
    if select == 1:
        sumimpstroke += min(stroke, par + 2)
    sumstroke += stroke
    sumpar += par
handicap = math.floor(0.8 * (1.5 * sumimpstroke - sumpar))
print(sumstroke)
print(handicap)
print(sumstroke - handicap)
