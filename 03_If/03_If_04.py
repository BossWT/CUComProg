num = input()
if (len(num) == 10 and num[0] == '0'):
    if (num[1] == '6' or num[1] == '8' or num[1] == '9'):
        print('Mobile number')
    else:
        print('Not a mobile number')
else:
    print('Not a mobile number')
