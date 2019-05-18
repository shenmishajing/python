n = int(input())

e, l = 0, 0

for i in range(n):
    g = eval(input())
    for key in g.keys():
        subg = g[key]
        e += len(subg)
        for v in subg:
            l += subg[v]

print(n, e, l)
