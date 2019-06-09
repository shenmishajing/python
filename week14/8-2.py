f = open('letter.txt', 'r', encoding='utf-8')

s = f.read()

f.close()

d = dict()

for c in s:
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1

f = open('result.txt', 'w', encoding='utf-8')

f.write(str(d))
