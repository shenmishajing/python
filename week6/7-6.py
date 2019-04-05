n = int(input())
if n == 0:
    print("average = 0.0")
    print("count = 0")
else:
    score = list(int(x) for x in input().split())
    # count = [x >= 60 for x in score]
    count = 0
    sum = 0
    for i in score:
        if i >= 60:
            count += 1
        sum += i

    print("average = %.1f" % (sum / n))
    print("count = %d" % count)
