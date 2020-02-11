ids = []
grades = []
pattern = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
while True:
    st = input()
    if st == 'q':
        break
    x, y = st.split()
    ids.append(x)
    grades.append(y)
uids = [x for x in input().split()]
for i in uids:
    if i in ids:
        index = ids.index(i)
        if pattern.index(grades[index]) != 0:
            grades[index] = pattern[pattern.index(grades[index]) - 1]
for i in range(len(ids)):
    print(ids[i], grades[i])
