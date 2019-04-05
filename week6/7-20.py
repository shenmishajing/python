direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def inner(i, j, matrix):
    if i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0]):
        return 1
    return 0


def localMin(matrix, i, j):
    for di in direction:
        if inner(i + di[0], j + di[1], matrix) == 0 or matrix[i][j] <= matrix[i + di[0]][j + di[1]]:
            return 0
    return 1


m, n = [int(x) for x in input().split()]

matrix = []

for i in range(m):
    matrix.append([int(x) for x in input().split()])

flag = 1

for i in range(m):
    for j in range(n):
        if localMin(matrix, i, j):
            print(matrix[i][j], i + 1, j + 1)
            flag = 0
if flag:
    print("None %d %d" % (m, n))
