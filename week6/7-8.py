import math
import statistics as st


def prime(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i) == 0:
            return 0

    return 1


price = [0, 3, 2.5, 4.1, 10.2]

print("[1] apple")
print("[2] pear")
print("[3] orange")
print("[4] grape")
print("[0] exit")

command = [int(x) for x in input().split()]
for count, i in enumerate(command):
    if i == 0 or count > 4:
        break
    else:
        if i < 1 or i > 4:
            i = 0
        print("price = %.2f" % (price[i]))
