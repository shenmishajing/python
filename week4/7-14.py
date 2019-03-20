s = input()

for c in s:
    if c == '#':
        break
    elif c.isupper():
        print(c.lower(), end='')
    elif c.islower():
        print(c.upper(), end='')
    else:
        print(c, end='')
