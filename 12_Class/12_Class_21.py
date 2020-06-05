class Complex:
    def __init__(self, a, b):
        self.a = str(a)
        self.b = str(b)

    def __str__(self):
        a = self.a
        b = self.b
        if a == "0" and b == "0":
            num = "0"
        elif a == "0":
            if b == "1":
                num = "i"
            elif b == "-1":
                num = "-i"
            else:
                num = b + "i"
        elif b == "0":
            num = a
        elif b == "-1":
            num = a + "-i"
        elif b == "1":
            num = a + "+i"
        else:
            if b[0] == "-":
                num = a + b + "i"
            else:
                num = a + "+" + b + "i"
        return num

    def __add__(self, rhs):
        suma = int(self.a) + int(rhs.a)
        sumb = int(self.b) + int(rhs.b)
        return Complex(suma, sumb)

    def __mul__(self, rhs):
        a = int(self.a)
        b = int(self.b)
        c = int(rhs.a)
        d = int(rhs.b)
        mula = (a * c) - (b * d)
        mulb = (a * d) + (b * c)
        return Complex(mula, mulb)

    def __truediv__(self, rhs):
        a = int(self.a)
        b = int(self.b)
        c = int(rhs.a)
        d = int(rhs.b)
        denom = (c**2) + (d**2)
        diva = ((a * c) + (b * d)) / denom
        divb = ((-a * d) + (b * c)) / denom
        return Complex(diva, divb)


t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1 + c2)
elif t == 4:
    print(c1 * c2)
else:
    print(c1 / c2)
