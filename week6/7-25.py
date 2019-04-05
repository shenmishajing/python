num = [int(x) for x in input().split()]

matrix = []
matrix.append(num[:3])
matrix.append(num[3:6])
matrix.append(num[6:])

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print("%4d" % (matrix[j][i]), end="")
    print()
