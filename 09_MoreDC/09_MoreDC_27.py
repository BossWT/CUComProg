def knows(R, x, y):
    if y in R[x]:
        return True
    return False
    # return True if x knows y


def is_celeb(R, x):  # return True if a is celeb, otherwise return False
    for e in R[x]:
        if e != x:
            return False
    for k in R.keys():
        if k != x and not knows(R, k, x):
            return False
    return True
    # return False if x knows someone who is not him/herself
    # return False if there exists someone in R who don't know x
    # otherwise return True


def find_celeb(R):
    for x in R.keys():
        if is_celeb(R, x):
            return x
    return None
    # for each person x in the party
    # if x is celeb --> return x
    # if no celeb in the party --> return None


def read_relations():
    pass
    # build a dictionary R from inputs
    # whose structure is shown in the example
    R = {}
    while True:
        d = input().split()
        if len(d) == 1:
            break
        if d[0] not in R:
            R[d[0]] = set()
        if d[1] not in R:
            R[d[1]] = set()
        R[d[0]].add(d[1])
    return R


def main():
    R = read_relations()
    c = find_celeb(R)
    if c is None:
        print('Not Found')
    else:
        print(c)


exec(input().strip())
