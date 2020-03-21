def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m


def mult_c(c, A):
    ans = [[col * c for col in row] for row in A]
    return ans


def mult(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    ans = []
    for i in range(n):
        c = []
        for j in range(p):
            sum = 0
            for k in range(m):
                sum += A[i][k] * B[k][j]
            c.append(sum)
        ans.append(c)
    return ans


exec(input().strip())
