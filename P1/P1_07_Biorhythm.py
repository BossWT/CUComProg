import math
bd, bm, by, d, m, y = [int(e) for e in input().split()]
by -= 543
y -= 543
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
feb = 0
if by % 400 == 0:
    day[2] = 29
elif by % 4 == 0 and by % 100 != 0:
    day[2] = 29
daysum = 0
daysum += day[bm] - bd + 1
for i in range(bm + 1, 13):
    daysum += day[i]
daysum += 365 * (y - by - 1)
day[2] = 28
if y % 400 == 0:
    day[2] = 29
elif y % 4 == 0 and y % 100 != 0:
    day[2] = 29
for i in range(1, m):
    daysum += day[i]
daysum += d - 1
physical = math.sin(2 * math.pi * daysum / 23)
emotional = math.sin(2 * math.pi * daysum / 28)
intellectual = math.sin(2 * math.pi * daysum / 33)
print(daysum, "{:.2f}".format(physical), "{:.2f}".format(emotional), "{:.2f}".format(intellectual))
