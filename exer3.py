from math import *
eps = float(input('Введіть значення для епсілона : '))
x = float(input('Введіть значення для x : '))
l1 = sin(x)/x
n = int(input('Введіть значення для n : '))
counter = 0
for i in range(n):
    counter += ((-1)**i)*x**i/factorial(i+1)
eps1 = abs(counter-l1)
if eps1 <= eps:
    print(True)
else:
    print(False)