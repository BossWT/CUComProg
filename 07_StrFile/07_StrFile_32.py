def no_lowercase(pwd):
    for c in pwd:
        if c.islower():
            return False
    return True


def no_uppercase(pwd):
    for c in pwd:
        if c.isupper():
            return False
    return True


def no_number(pwd):
    for c in pwd:
        if c.isnumeric():
            return False
    return True


def no_symbol(pwd):
    for c in pwd:
        if not c.isalnum():
            return False
    return True


def character_repetition(pwd):
    for i in range(len(pwd) - 3):
        if pwd[i] == pwd[i + 1] and pwd[i] == pwd[i + 2] and pwd[i] == pwd[i + 3]:
            return True
    return False


def number_sequence(pwd):
    num = '01234567890'
    rnum = num[::-1]
    for i in range(len(pwd) - 3):
        if num.find(pwd[i: i + 4]) != -1:
            return True
        if rnum.find(pwd[i: i + 4]) != -1:
            return True
    return False


def letter_sequence(pwd):
    pwd = pwd.lower()
    let = 'abcdefghijklmnopqrstuvwxyz'
    rlet = let[::-1]
    for i in range(len(pwd) - 3):
        if let.find(pwd[i: i + 4]) != -1:
            return True
        if rlet.find(pwd[i: i + 4]) != -1:
            return True
    return False


def keyboard_pattern(pwd):
    pwd = pwd.lower()
    pattern = ['!@#$%^&*()_+', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    rpattern = []
    for row in pattern:
        rpattern.append(row[::-1])
    for i in range(len(pwd) - 3):
        for j in range(4):
            if pattern[j].find(pwd[i: i + 4]) != -1:
                return True
            if rpattern[j].find(pwd[i: i + 4]) != -1:
                return True
    return False


pwd = input().strip()
errors = []
if len(pwd) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(pwd):
    errors.append("No lowercase letters")
if no_uppercase(pwd):
    errors.append("No uppercase letters")
if no_number(pwd):
    errors.append('No numbers')
if no_symbol(pwd):
    errors.append('No symbols')
if character_repetition(pwd):
    errors.append('Character repetition')
if number_sequence(pwd):
    errors.append('Number sequence')
if letter_sequence(pwd):
    errors.append('Letter sequence')
if keyboard_pattern(pwd):
    errors.append('Keyboard pattern')
if len(errors) == 0:
    print('OK')
else:
    for i in errors:
        print(i)
