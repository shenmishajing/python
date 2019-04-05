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

n = int(input())

for i in range(1, n + 1):
    factor *= i
    sum += 1 / factor

print("{:.8f}".format(sum))
