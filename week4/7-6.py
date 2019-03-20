L = [int(x) for x in input().split()]

x = {a: L.count(a) for a in L}
# y = [(k, v) for k, v in x.items() if max(x.values()) == v]
for k, v in x.items():
    if max(x.values()) == v:
        print(k, v)
