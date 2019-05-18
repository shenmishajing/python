from functools import cmp_to_key

first = eval(input())
second = eval((input()))

for key in second.keys():
    if key in first:
        first[key] += second[key]
    else:
        first[key] = second[key]


def cmp(x, y):
    if type(x) == type(y):
        if x > y:
            return 1
        elif x == y:
            return 0
        else:
            return -1
    elif isinstance(x, int) and isinstance(y, str):
        return -1
    else:
        return 1


keys = sorted(list(first.keys()), key=cmp_to_key(cmp))

print('{', end='')

f = 1

for key in keys:
    if f:
        f = 0
    else:
        print(',', end='')
    if isinstance(key, str):
        print('"{}":{}'.format(key, first[key]), end='')
    else:
        print('{}:{}'.format(key, first[key]), end='')
print('}', end='')
