n = int(input())

sum = 0

for i in range(n - 1):
    num = [int(x) for x in input().split()]
    for j, x in enumerate(num[:-1]):
        if j != n - i - 1:
            sum += x

print(sum)
