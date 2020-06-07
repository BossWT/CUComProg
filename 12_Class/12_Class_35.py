class roman:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def __init__(self, r):
        self.r = r

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        return self.r

    def __int__(self):
        r = self.r
        num = 0
        for i in range(len(r)):
            value = roman.values[r[i]]
            if i < len(r) - 1:
                if roman.values[r[i]] < roman.values[r[i + 1]]:
                    value = -value
            num += value
        return num

    def __add__(self, rhs):
        num = int(self) + int(rhs)
        num_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        res = ""
        while num > 0:
            for i, r in num_map:
                while num >= i:
                    res += r
                    num -= i
        return roman(res)


t, r1, r2 = input().split()
a = roman(r1)
b = roman(r2)
if t == "1":
    print(a < b)
elif t == "2":
    print(int(a), int(b))
elif t == "3":
    print(str(a), str(b))
elif t == "4":
    print(int(a + b))
else:
    print(str(a + b))
