def calculate(l, k):
    sum = 0
    for item in l:
        if isinstance(item, list) or isinstance(item, tuple):
            sum += calculate(item, k+1)
        elif isinstance(item, str):
            continue
        else:
            sum += k
    return sum


l = eval(input())

print(calculate(l, 1))
