c_name = input()
t_name = input()
db_name = input()
c_dict = {}
t_dict = {}
db_dict = {}
courses = open(c_name, 'r')
teachers = open(t_name, 'r')
database = open(db_name, 'r')
for line in courses:
    data = line.rstrip().split(',')
    c_dict[data[0]] = data[1]
for line in teachers:
    data = line.rstrip().split(',')
    t_dict[data[0]] = data[1]
for line in database:
    data = line.rstrip().split(',')
    if data[0] in c_dict and data[1] in t_dict:
        print(c_dict[data[0]] + ',' + t_dict[data[1]])
    else:
        print('record error')
