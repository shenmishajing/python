n = int(input())

count = 0

for i in range(n // 5, 0, -1):
    for j in range((n - 5 * i) // 2, 0, -1):
        if n - 5 * i - 2 * j:
            print("fen5:%d, fen2:%d, fen1:%d, total:%d" % (i, j, n - 5 * i - 2 * j, n - 4 * i - j))
            count += 1

print("count = %d" % (count))
