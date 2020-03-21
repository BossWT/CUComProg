def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True


def next_prime(n):
    i = n + 1
    while True:
        if (is_prime(i)):
            return i
        i += 1


def factor(n):
    k = 2
    ans = []
    while k <= n:
        power = 0
        while n % k == 0:
            n /= k
            power += 1
        if power > 0:
            ans.append([k, power])
        k = next_prime(k)
    return ans


exec(input().strip())
