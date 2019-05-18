first = int(input())
op = input()
second = int(input())

if op == '+':
    print("%.2f" % (first + second))
elif op == '-':
    print("%.2f" % (first - second))
elif op == '*':
    print("%.2f" % (first * second))
elif op == '/':
    if second:
        print("%.2f" % (first / second))
    else:
        print('divided by zero')
