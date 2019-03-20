s = input()

l = []

for c in s:
    if c.isupper() and c not in l:
        l.append(c)
if l == []:
    print('Not Found')
else:
    for c in l:
        print(c, end='')
