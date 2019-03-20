s = input()

for c in s:
    if c.isupper():
        print(chr(ord('Z') - (ord(c) - ord('A'))), end='')
    else:
        print(c, end='')
