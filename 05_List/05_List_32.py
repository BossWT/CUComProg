n = int(input())
time = []
waitsum = 0
numq = 0
latest_time = 0
for i in range(n):
    op = input().split()
    if op[0] == 'reset':
        q_num = int(op[1])
        cur_q = q_num
    elif op[0] == 'new':
        time.append(op[1])
        print('ticket', q_num)
        q_num += 1
    elif op[0] == 'next':
        print('call', cur_q)
        latest_time = int(time[0])
        time.pop(0)
        cur_q += 1
    elif op[0] == 'order':
        waittime = int(op[1]) - latest_time
        print('qtime', cur_q - 1, waittime)
        waitsum += waittime
        numq += 1
    elif op[0] == 'avg_qtime':
        print('avg_qtime', round(waitsum / numq, 4))
