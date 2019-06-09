f = open('freedom.txt', 'r', encoding='utf-8')

s = f.readlines()

f.close()

f = open('dic.txt', 'w', encoding='utf-8')

text = u''

for c in s:
    text += c

print(text)
text = text.lower()

stop_words = [',', '.', ':', ';', '"', '，', '。', '：', '“', '”', '；']

for c in stop_words:
    text = text.replace(c, ' ')

d = dict()

# for c in text:
#     if not(u'a' <= c <= u'z'):
#         text.replace(c, ' ')

print(text)

temp = text.split()

for c in temp:
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1

l = [x for x in d.items()]

l.sort(key=lambda x: x[0])

for c in l:
    f.write('{}:{}\n'.format(c[0], c[1]))

f.close()
