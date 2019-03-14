num = [int(x) for x in input().split()]

s = sum(num)

if s - max(num) <= max(num):
    print("These sides do not correspond to a valid triangle")
else:
    s /= 2
    t = [s - x for x in num]
    print("area = %.2f; perimeter = %.2f" % (pow(s * t[1] * t[0] * t[2], 0.5),
                                             2 * s))
