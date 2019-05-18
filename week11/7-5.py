l = [int(x) for x in input().split(',')]
sec = range(6, 11)

res = [x for x in sec if x not in l]

first = 1

for item in res:
    if first:
        first = 0
    else:
        print(' ', end='')
    print(item, end='')
