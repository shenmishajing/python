num = [int(x) for x in input().split()]

num.sort()

print(*num, sep="->")
