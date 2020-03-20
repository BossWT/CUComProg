def delivery(id, t, d, m, y):
    dur = duration[types.index(t)]
    maxday = days[m - 1]
    d += dur
    if d > maxday:
        d -= maxday
        m += 1
    if m > 12:
        m = 1
        y += 1
    data = [y, m, d, id]
    return data


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
types = ['E', 'Q', 'N', 'F']
duration = [1, 3, 7, 14]
errors = []
ans = []
while True:
    order = input().strip()
    if order == 'END':
        break
    order = order.split()
    d_id = order[0]
    d_type = order[1]
    d_day = int(order[2])
    d_mon = int(order[3])
    d_year = int(order[4])
    if (d_year - 543) % 400 == 0 or ((d_year - 543) % 4 == 0 and (d_year - 543) % 100 != 0):
        days[1] = 29
    else:
        days[1] = 28
    if d_year < 2558:
        err = 'Error: ' + str(d_id) + ' ' + str(d_type) + ' ' + str(d_day) + ' ' + \
            str(d_mon) + ' ' + str(d_year) + ' --> Invalid year'
        errors.append(err)
        continue
    if d_mon < 1 or d_mon > 12:
        err = 'Error: ' + str(d_id) + ' ' + str(d_type) + ' ' + str(d_day) + ' ' + \
            str(d_mon) + ' ' + str(d_year) + ' --> Invalid month'
        errors.append(err)
        continue
    if d_day < 1 or d_day > days[d_mon - 1]:
        err = 'Error: ' + str(d_id) + ' ' + str(d_type) + ' ' + str(d_day) + ' ' + \
            str(d_mon) + ' ' + str(d_year) + ' --> Invalid date'
        errors.append(err)
        continue
    if d_type not in types:
        err = 'Error: ' + str(d_id) + ' ' + str(d_type) + ' ' + str(d_day) + ' ' + \
            str(d_mon) + ' ' + str(d_year) + ' --> Invalid delivery type'
        errors.append(err)
        continue
    ans.append(delivery(d_id, d_type, d_day, d_mon, d_year))
for e in errors:
    print(e)
ans.sort()
for e in ans:
    print(str(e[-1]) + ': delivered on ' + str(e[2]) + '/' + str(e[1]) + '/' + str(e[0]))
