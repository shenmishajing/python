def calculate(l):
    sum = 0
    for item in l:
        if isinstance(item, list) or isinstance(item, tuple):
            sum += calculate(item)
        elif isinstance(item, str):
            continue
        else:
            sum += item
    return sum


l = eval(input())

print(calculate(l))
