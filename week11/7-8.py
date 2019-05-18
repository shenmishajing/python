numbers = [int(x) for x in input().split(',')]
target = int(input())

need_number = [target - number for number in numbers]

flag = 1

for index, number in enumerate(need_number):
    if number in numbers:
        print(index, numbers.index(number))
        flag = 0
        break

if flag:
    print('no answer')
