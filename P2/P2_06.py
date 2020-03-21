def t2m(pattern, text):
    morse = ''
    for e in text:
        j = pattern.find('[' + e + ']')
        if j == -1:
            return 'Invalid : ' + text
        j += 3
        k = pattern.find('[', j)
        morse += pattern[j:k] + ' '
    return morse.strip()


def m2t(pattern, morse):
    text = ''
    morse = morse.split()
    for e in morse:
        j = pattern.find(']' + e + '[')
        if j == -1:
            return 'Invalid : ' + ' '.join(morse)
        text += pattern[j - 1]
    return text


filename = input().strip()
f = open(filename, 'r')
data = []
for line in f:
    line = line.replace('\n', '')
    data.append(line)
mode = data[0]
pattern = data[1]
if mode == 'T2M':
    for i in range(2, len(data)):
        print(t2m(pattern, data[i]))
elif mode == 'M2T':
    for i in range(2, len(data)):
        print(m2t(pattern, data[i]))
else:
    print('Invalid code')
