import math
import statistics as st


def prime(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i) == 0:
            return 0

    return 1


first = 2
second = 1
sum = 0

n = int(input())
for i in range(n):
    sum += first / second
    first, second = first + second, first

print("%.2f" % (sum))
