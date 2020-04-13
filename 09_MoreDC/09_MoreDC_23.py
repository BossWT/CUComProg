n = int(input())


def addTime(old, new):
    old = old.split(':')
    new = new.split(':')
    m_old = int(old[0])
    s_old = int(old[1])
    m_new = int(new[0])
    s_new = int(new[1])
    s_sum = s_old + s_new
    m_sum = m_old + m_new + s_sum // 60
    s_sum %= 60
    if s_sum < 10:
        s_sum = '0' + str(s_sum)
    return str(m_sum) + ':' + str(s_sum)


d_genre = {}
for i in range(n):
    data = input().split(', ')
    if data[2] in d_genre:
        d_genre[data[2]] = addTime(d_genre[data[2]], data[3])
    else:
        d_genre[data[2]] = data[3]
ans = []
for k, v in d_genre.items():
    v = float(v.replace(':', '.'))
    ans.append([-v, k])
ans.sort()
for i in range(len(ans)):
    ans[i][0] = str(ans[i][0] * -1)
    temp = ans[i][0].split('.')
    if len(temp[1]) == 1:
        temp[1] += '0'
    ans[i][0] = ':'.join(temp)
    print(ans[i][1], '-->', ans[i][0])
    if i == 2:
        break
