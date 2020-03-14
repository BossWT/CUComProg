def is_odd(n):
    if n % 2:
        return True
    return False


def has_odds(x):
    for i in x:
        if i % 2:
            return True
    return False


def all_odds(x):
    for i in x:
        if i % 2 == 0:
            return False
    return True


def no_odds(x):
    for i in x:
        if i % 2:
            return False
    return True


def get_odds(x):
    ans = []
    for i in x:
        if i % 2:
            ans.append(i)
    return ans


def zip_odds(a, b):
    a = get_odds(a)
    b = get_odds(b)
    ans = []
    while len(a) != 0 or len(b) != 0:
        if len(a) != 0:
            ans.append(a.pop(0))
        if len(b) != 0:
            ans.append(b.pop(0))
    return ans


exec(input().strip())
