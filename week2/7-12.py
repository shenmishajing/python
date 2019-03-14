n, m = [int(x) for x in input().split()]

if n <= m:
    print("fahr celsius")
    for i in range(n, m + 1, 2):
        print("%d%6.1f" % (i, 5 * (i - 32) / 9))
else:
    print("Invalid.")
