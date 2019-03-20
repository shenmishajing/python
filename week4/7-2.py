n = int(input())

weight = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
table = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
wrong = []
count = 0

for i in range(n):
    s = input()
    x = list(s)
    flag = 0
    for c in x[:-1]:
        if c not in number:
            flag = 1
            break

    if flag:
        count += 1
        wrong.append(s)
    else:
        check = x[-1]
        x = [int(b) for b in x[:-1]]
        sum = 0
        for j, c in enumerate(x):
            sum += c * weight[j]
        if table[sum % 11] != check:
            count += 1
            wrong.append(s)

if count == 0:
    print("All passed")
else:
    for s in wrong:
        print(s)
