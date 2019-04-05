def factor(n):
    f = 1
    for i in range(n):
        f *= i + 1
    return f


n = int(input())

sum = 0

for i in range(0, n + 1, 2):
    sum += factor(i + 1)

print("n=%d,s=%d" % (n, sum))
