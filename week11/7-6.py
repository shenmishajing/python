a, b = [int(x) for x in input().split()]

count = 0

for i in range(a, b + 1):
    if not i % 3 and not i % 5 and not i % 7:
        count += 1

print(count)
