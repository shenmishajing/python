import math
import statistics as st


def prime(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i) == 0:
            return 0

    return 1


def gcd(a, b):
    a, b = (a, b) if a >= b else (b, a)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


n, m = [int(x) for x in input().split()]

print(gcd(n, m), lcm(n, m))
