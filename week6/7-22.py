n = int(input())

c = "A"

for i in range(n):
    for j in range(i, n):
        print(c, end=" ")
        c = chr(ord(c) + 1)
    print()
