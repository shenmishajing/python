n = int(input())

max_order, max_name, max_mark = None, None, None

for i in range(n):
    order, name, a, b, c = input().split()
    mark = sum([int(x) for x in (a, b, c)])
    if max_mark is None or max_mark < mark:
        max_order, max_name, max_mark = order, name, mark

print(max_name, max_order, max_mark)
