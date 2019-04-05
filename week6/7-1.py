import math

n = int(input())

for i in range(n + 1):
    print("pow(3,{}) = {:.0f}".format(i, math.pow(3, i)))
