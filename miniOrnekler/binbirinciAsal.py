import numpy as np
from math import sqrt
from itertools import count, islice


def asalMi(x):
    return x > 1 and all(x % i for i in islice(count(2), int(sqrt(x) - 1)))

sayac = 0
sayi = 2
while True:
    if asalMi(sayi):
        sayac += 1
    if sayac == 10001:
        break
    sayi += 1

print(sayi)








