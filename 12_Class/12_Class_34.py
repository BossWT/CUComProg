class piggybank:
    def __init__(self):
        self.coins = {}
        self.total_coins = 0

    def add(self, v, n):
        if self.total_coins + n > 100:
            return False
        v = float(v)
        if v not in self.coins:
            self.coins[v] = 0
        self.coins[v] += n
        self.total_coins += n
        return True

    def __float__(self):
        total_values = 0.0
        for coin, n in self.coins.items():
            total_values += coin * n
        return total_values

    def __str__(self):
        res = "{"
        for coin, n in sorted(self.coins.items()):
            res += str(coin) + ":" + str(n) + ", "
        if len(res) > 1:
            res = res[:-2]
        res += "}"
        return res


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank()
p2 = piggybank()
for c in cmd1:
    eval(c)
for c in cmd2:
    eval(c)
