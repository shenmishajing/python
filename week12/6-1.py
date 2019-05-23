def fn(a, n):
    sum = 0
    number = a
    for i in range(n):
        sum += number
        number *= 10
        number += a
    return sum


/* 请在这里填写答案 * /

a, b = input().split()
s = fn(int(a), int(b))
print(s)
