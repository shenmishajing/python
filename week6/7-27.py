m, n = [int(x) for x in input().split()]

factors = [[1, 2, 3], [1, 2, 4, 7, 14], [1, 2, 4, 8, 16, 31, 62, 124, 248],
           [1, 2, 4, 8, 16, 32, 64, 127, 254, 508, 1016, 2032, 4064]]

numbers = [6, 28, 496, 8128]

pr = 0

for num, factor in zip(numbers, factors):
    if num >= m and num <= n:
        pr = 1
        print("%d = " % num, end="")
        first = 1
        for x in factor:
            if first == 0:
                print(" + ", end="")
            else:
                first = 0
            print(x, end="")
        print()
if pr == 0:
    print("None")
