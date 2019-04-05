import math


def prime(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i) == 0:
            return 0

    return 1


first = 0
second = 1

n = int(input())

for i in range(n):
    first += second
    second = first - second
    if first > n:
        print(first)
        break
