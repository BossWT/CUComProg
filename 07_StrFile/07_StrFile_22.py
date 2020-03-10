anagram = True
str1 = input()
str2 = input()
str1 = str1.lower()
str2 = str2.lower()
str1 = str1.replace(' ', '')
str2 = str2.replace(' ', '')
len1 = len(str1)
len2 = len(str2)
if len1 != len2:
    anagram = False
else:
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len1):
        if str1[i] != str2[i]:
            anagram = False
            break
if (anagram):
    print('YES')
else:
    print('NO')
