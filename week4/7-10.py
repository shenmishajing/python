s = input()

table = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

count = 0

for c in s:
    if c.isupper() and c not in table:
        count += 1

print(count)
