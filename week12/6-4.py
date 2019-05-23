def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def PrintFN(m, n):
    res = []
    cur = 1
    cur_number = fib(cur)
    while cur_number < n:
        if m <= cur_number <= n:
            res.append(cur_number)
        cur += 1
        cur_number = fib(cur)
    return res


m, n, i = input().split()
n = int(n)
m = int(m)
i = int(i)
b = fib(i)
print("fib({0}) = {1}".format(i, b))
fiblist = PrintFN(m, n)
print(len(fiblist))
