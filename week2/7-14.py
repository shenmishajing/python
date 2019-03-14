n, m = [int(x) for x in input().split()]

sum = 0

flag = 1

for i, cur in enumerate(range(n, m + 1)):
    print("%5d" % cur, end="")
    sum += cur
    if (i + 1) % 5 == 0:
        print()
        flag = 0
    else:
        flag = 1
if flag:
    print()

print("Sum = %d" % sum)
