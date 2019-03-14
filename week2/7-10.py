n = int(input())

sum = 0

for i in range(n):
    sum += 1 / (2 * i + 1)

print("sum = %.6f" % sum)
