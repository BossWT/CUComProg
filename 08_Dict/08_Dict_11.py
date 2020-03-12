def reverse(d):
    return {a: b for b, a in d.items()}


def keys(d, v):
    res = []
    for key, value in d.items():
        if value == v:
            res.append(key)
    return res


exec(input().strip())
