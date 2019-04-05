import math


def prime(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i) == 0:
            return 0

    return 1


n = int(input())

for i in range(2, n):
    if prime(i) and prime(n - i):
        print("{} = {} + {}".format(n, i, n - i))
        break
