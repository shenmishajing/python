def prime(x):
    if x == 1:
        return 0
    for i in range(2, x):
        if (x % i) == 0:
            return 0

    return 1


n, m = [int(x) for x in input().split()]

count = 0
sum = 0

for i in range(n, m + 1):
    if prime(i):
        count += 1
        sum += i

print(count, sum)
