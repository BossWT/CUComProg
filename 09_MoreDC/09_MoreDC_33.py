def add_poly(p1, p2):
    d = {}
    ans = []
    for var, exp in p1:
        d[exp] = var
    for var, exp in p2:
        if exp in d:
            d[exp] = d[exp] + var
        else:
            d[exp] = var
    for k, v in sorted(d.items(), reverse=True):
        if v != 0:
            ans.append((v, k))
    return ans


def mult_poly(p1, p2):
    d = {}
    ans = []
    for var1, exp1 in p1:
        for var2, exp2 in p2:
            if exp1 + exp2 in d:
                d[exp1 + exp2] += (var1 * var2)
            else:
                d[exp1 + exp2] = (var1 * var2)
    for k, v in sorted(d.items(), reverse=True):
        if v != 0:
            ans.append((v, k))
    return ans


for i in range(3):
    exec(input().strip())
