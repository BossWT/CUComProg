import math
w = float(input())
h = float(input())
m = math.sqrt(w*h)/60
hay = 0.024265*pow(w, 0.5378)*pow(h, 0.3964)
b = 0.0333*pow(w, (0.6157-(0.0188*math.log(w, 10))))*pow(h, 0.3)
print(m)
print(hay)
print(b)