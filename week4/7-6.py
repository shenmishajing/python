from collections import Counter

# L = [int(x) for x in input().split()]
L = input().split()[1:]
# x = {a: L.count(a) for a in L}
# y = [(k, v) for k, v in x.items() if max(x.values()) == v]
# for k, v in x.items():
#    if max(x.values()) == v:
#        print(k, v)
for k, v in Counter(L).most_common(1):
    print(k, v)
