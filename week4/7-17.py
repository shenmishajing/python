s = input().strip()
c = input().strip()

s = s.replace(c, '')
s = s.replace(c.upper() if c.islower() else c.lower(), '')

print("result:", s)
