d = {}


def gendict():
    #######################
    # Below is algorithm to generate dictionary for text convert
    # if you don't understand you can use convetional way by manually input data
    count = 1
    num = '2'
    maxcount = 3
    for i in range(26):
        d[chr(97 + i)] = num * count
        d[num * count] = chr(97 + i)
        if count == maxcount:
            num = chr(ord(num) + 1)
            count = 0
        if num == '7' or num == '9':
            maxcount = 4
        else:
            maxcount = 3
        count += 1
    d[' '] = '0'
    d['0'] = ' '
    #########################


def reverse(d):
    nd = {}
    for k, v in d.items():
        nd[v] = k
    return nd


def text2keys(text):
    text = text.lower()
    keys = ''
    for c in text:
        if c.isalnum() or c == ' ':
            keys += d[c]
        keys += ' '
    return keys


def keys2text(keys):
    code = keys.split()
    text = ''
    for i in code:
        text += d[i]
    return text


gendict()
exec(input().strip())
