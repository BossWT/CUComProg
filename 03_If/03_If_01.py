fac = ['01', '02']
for i in range(20, 41):
    fac.append(str(i))
fac.append('51')
fac.append('53')
fac.append('55')
fac.append('58')
n = input()
if n in fac:
    print('OK')
else:
    print('Error')
