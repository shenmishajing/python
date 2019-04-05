import statistics as st

num = [int(x) for x in input().split()]

matrix = []
matrix.append(num[:3])
matrix.append(num[3:6])
matrix.append(num[6:])

for num in matrix:
    for x in num:
        print("%4d" % (x), end="")

    print("%4d" % (max(num)), end="")
    print("%4d" % (sum(num)))
