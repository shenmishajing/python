import re

s = input()
c = input().split()

for i in c[::-1]:
    for m in list(re.finditer(i, s))[::-1]:
        print(m.start(), i)
