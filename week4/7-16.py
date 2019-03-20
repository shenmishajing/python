s = input()
x = list(set(s))
for c in sorted(x):
    print(c, end='')
