name = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nickname = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']
n = int(input())
for i in range(n):
    st = input()
    if st in name:
        index = name.index(st)
        print(nickname[index])
    elif st in nickname:
        index = nickname.index(st)
        print(name[index])
    else:
        print('Not found')
