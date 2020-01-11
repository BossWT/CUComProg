str = input()
month = ['x', 'January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']
date = str.split('/')
day = date[0]
mon = date[1]
year = date[2]
print(month[int(mon)], day + ',', year, sep=' ')
