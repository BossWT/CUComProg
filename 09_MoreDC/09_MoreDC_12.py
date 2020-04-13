n = int(input())
intersect = set()
union = set()
for i in range(n):
    num = [int(x) for x in input().split()]
    num = set(num)
    if i == 0:
        intersect = set(num)
    else:
        intersect = intersect.intersection(num)
    union = union.union(num)
print(len(union))
print(len(intersect))
