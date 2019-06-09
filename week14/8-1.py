f = open('example.txt', 'r', encoding='utf-8')

s = f.read()

f.close()

f = open('result.txt', 'w', encoding='utf-8')

f.write(s.lower())
