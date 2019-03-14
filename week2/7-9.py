a, n = [int(x) for x in input().split()]

sum = 0

for i in range(n):
    sum *= 10
    sum += (i + 1) * a

print("s = %d" % sum)
