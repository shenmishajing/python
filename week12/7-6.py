def calculate(l, k):
    sum = 0
    for item in l:
        if isinstance(item, list) or isinstance(item, tuple):
            sum += calculate(item, k-1)
        elif isinstance(item, str):
            continue
        else:
            if k == 1:
                sum += 1
    return sum


l = eval(input())
n = int(input())

print(calculate(l, n))
