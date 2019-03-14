n, m = [int(x) for x in input().split()]

sum = 0

for i in range(n, m + 1):
    sum += i**2 + 1 / i

print("sum = %.6f" % sum)
