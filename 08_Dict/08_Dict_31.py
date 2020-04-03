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
    # Using list to display certain order
    a = {}
    new = {}
    z = []
    for s in pocket:
        z.append([s * -1, pocket[s]])
    z.sort()
    for e in z:
        e[0] = int(e[0]) * -1
    for e in range(len(z)):
        while z[e][0] <= amt and z[e][1] != 0:
            if z[e][0] not in a:
                z[e][1] -= 1
                a[z[e][0]] = 1
                amt -= z[e][0]
            else:
                z[e][1] -= 1
                amt -= z[e][0]
                a[z[e][0]] += 1
    if amt != 0:
        return {}
    for e in range(len(z)):
        new[z[e][0]] = z[e][1]
    for e in new:
        pocket[e] = new[e]
    return a
    # Use .items() will display uncertain order of key and value in older python version.
    # d_pay = {}
    # for k, v in pocket.items():
    #     while amt >= k and pocket[k] > 0:
    #         if k in d_pay:
    #             d_pay[k] += 1
    #         else:
    #             d_pay[k] = 1
    #         amt -= k
    #         pocket[k] -= 1
    # if amt == 0:
    #     return d_pay
    # else:
    #     for k, v in d_pay.items():
    #         pocket[k] += v
    #     return {}


exec(input().strip())
