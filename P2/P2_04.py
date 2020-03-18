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
    date = [d, m, y]
    deliver[id] = date


def sort_deliver(d):
    ans = {k: v for k, v in sorted(d.items(), key=lambda x: (x[1][2], x[1][1], x[1][0], x[0]))}
    return ans


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
deliver = {}
types = ['E', 'Q', 'N', 'F']
duration = [1, 3, 7, 14]
errors = []
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
    delivery(d_id, d_type, d_day, d_mon, d_year)
for e in errors:
    print(e)
deliver = sort_deliver(deliver)
for k, v in deliver.items():
    print(str(k) + ': delivered on ' + '/'.join(str(x) for x in v))
