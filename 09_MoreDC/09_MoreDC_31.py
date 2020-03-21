def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b, c):
    return gcd(a, gcd(b, c)) == 1


def exist(i, j, k, triple):
    for e in triple:
        if i in e and j in e and k in e:
            return True
    return False


def primitive_Pythagorean_triples(max_len):
    triple = []
    max_len += 1
    for i in range(1, max_len):
        for j in range(i + 1, max_len):
            for k in range(j + 1, max_len):
                if is_coprime(i, j, k) and k * k == i * i + j * j and not exist(i, j, k, triple):
                    triple.append([k, i, j])
    triple.sort()
    ans = []
    for i, j, k in triple:
        ans.append([j, k, i])
    return ans


exec(input().strip())
