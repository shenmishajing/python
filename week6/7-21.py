n = int(input())

for i in range(n):
    for j in range(i + 1):
        print("%d*%d=%-4d" % (j + 1, i + 1, (i + 1) * (j + 1)), end="")
    if i + 1 != n:
        print()
