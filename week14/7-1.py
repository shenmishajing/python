import sys

d = dict()

s = sys.stdin.read().lower()
s = s[:s.find('#')]

for c in s:
    if not ('0' <= c <= '9' or 'a' <= c <= 'z' or c == '_'):
        s = s.replace(c, ' ')

s = s.split()

for c in s:
    if len(c) > 15:
        c = c[0:15]
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1

l = [x for x in d.items()]

l.sort(key=lambda x: (-x[1], x[0]))

print(len(l))

num = len(l)//10
for i in range(0, num):
    print('{}:{}'.format(l[i][1], l[i][0]))
