n = int(input())

m = []

for i in range(n):
    m.append([int(x) for x in input().split()])

max_index = []

for i, row in enumerate(m):
    cur_index = []
    cur_max = row[0]
    for index, item in enumerate(row):
        if item > cur_max:
            cur_max = item
            cur_index = [index]
        elif item == cur_max:
            cur_index.append(index)
    max_index.append([i, cur_index])

count = 0

for i, indexes in max_index:
    for index in indexes:
        add = 1
        for l in m:
            if l[index] < m[i][index]:
                add = 0
                break
        count += add

print(count)
