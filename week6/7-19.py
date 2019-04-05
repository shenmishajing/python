m = int(input())

for i in range(m):
    flag = 0
    n = int(input())
    for j in range(n):
        num = [int(x) for x in input().split()]
        if flag == 0:
            for k, x in enumerate(num):
                if k < j and x:
                    print("NO")
                    flag = 1
                    break
    if flag == 0:
        print("YES")
