def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    return True


def PrimeSum(m, n):
    sum = 0
    for i in range(m, n+1):
        if prime(i):
            sum += i
    return sum


/* 请在这里填写答案 * /

m, n = input().split()
m = int(m)
n = int(n)
print(PrimeSum(m, n))
