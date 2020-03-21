def to_Thai(n):
    tempn = n
    if n == 0:
        call = 'soon'
    else:
        call = ''
        name = {0: 'soon', 1: 'neung', 2: 'song', 3: 'sam', 4: 'si',
                5: 'ha', 6: 'hok', 7: 'chet', 8: 'paet', 9: 'kao', 10: 'sip'}
        pun = int(n / 1000)
        if pun > 0:
            call += ' ' + name[pun]
            call += ' pun'
        n %= 1000
        roi = int(n / 100)
        if roi > 0:
            call += ' ' + name[roi]
            call += ' roi'
        n %= 100
        sip = int(n / 10)
        if sip > 0:
            if sip == 2:
                call += ' yi'
            elif sip > 2:
                call += ' ' + name[sip]
            call += ' sip'
        n %= 10
        if n > 0:
            if n == 1 and tempn > 1:
                call += ' et'
            else:
                call += ' ' + name[n]
    return call.strip()


exec(input().strip())
