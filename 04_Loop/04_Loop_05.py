word = input()
sen = input()
s = sen.replace('(', '')
s = s.replace('"', '')
s = s.replace(')', '')
s = s.replace("'", '')
s = s.replace('.', ' ')
words = s.split()
count = 0
for w in words:
    if word == w:
        count += 1
print(count)
