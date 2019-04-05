import math


def prime(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i) == 0:
            return 0

    return 1


sum = 1
factor = 1

n = float(input())

cur = 1

while 1:
    factor *= cur
    cur += 1
    if 1 / (factor / cur) >= n:
        sum += 1 / factor
    else:
        break

print("{:.6f}".format(sum))
