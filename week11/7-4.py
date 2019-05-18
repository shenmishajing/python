l = eval(input())
l = list({}.fromkeys(l).keys())

first = 1

for item in l:
    if first:
        first = 0
    else:
        print(' ', end='')
    print(item, end='')
