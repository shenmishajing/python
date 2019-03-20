s = input()

l = []

count = 0

for c in s:
    if c.isalpha() and c not in l:
        count += 1
        l.append(c)
    if count == 10:
        break

if count == 10:
    for c in l:
        print(c, end='')
else:
    print('not found')
