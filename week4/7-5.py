s = list(input())
flag = 0
for c in s:
    if c == '0':
        if flag:
            print(c, end='')

    if c > '0' and c <= '9':
        flag = 1
        print(c, end='')

if flag == 0:
    print('0')
