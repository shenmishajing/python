s = input()

l = []

flag = 0

table = '0123456789abcdefABCDEF'

for c in s:
    if c == '-' and l == []:
        flag = 1
    if c in table:
        l.append(c)
if l == []:
    n = 0
else:
    n = int(''.join(l), 16)
if flag:
    n = -n
print(n)
