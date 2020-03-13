def total(pocket):
    sum = 0
    for k, v in pocket.items():
        sum += k * v
    return sum


def take(pocket, money_in):
    for k, v in money_in.items():
        if k in pocket:
            pocket[k] += v
        else:
            pocket[k] = v
    return pocket


def pay(pocket, amt):
    d_pay = {}
    for k, v in pocket.items():
        while amt >= k and pocket[k] > 0:
            if k in d_pay:
                d_pay[k] += 1
            else:
                d_pay[k] = 1
            amt -= k
            pocket[k] -= 1
    if amt == 0:
        return d_pay
    else:
        for k, v in d_pay.items():
            pocket[k] += v
        return {}


exec(input().strip())
