n = int(input())
m = input()

for i in range(n - 1):
    s = input()
    if len(s) > len(m):
        m = s
print("The longest is:", m)
