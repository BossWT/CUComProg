def make_int_list(x):
    num = x.split()
    ans = []
    for i in num:
        ans.append(int(i))
    return ans


def is_odd(e):
    if e % 2 == 1:
        return True
    else:
        return False


def odd_list(alist):
    ans = []
    for i in alist:
        if i % 2 == 1:
            ans.append(i)
    return ans


def sum_square(alist):
    res = 0
    for i in alist:
        res += i * i
    return res


exec(input().strip())
