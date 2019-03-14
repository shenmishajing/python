n = int(input())

sum = 0

for i in range(n):
    sum += (i + 1) / (2 * i + 1) * pow(-1, i)

print("%.3f" % sum)
