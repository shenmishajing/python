def funcos(eps, x):
    res = 0
    x2 = x*x
    cur_number = 1
    cur_iteration = 0

    # while cur_number >= eps:
    #     cur_iteration += 2
    #     cur_number *= x2/(cur_iteration-1)/cur_iteration
    #     res += (-1)**(cur_iteration/2)*cur_number

    while cur_number >= eps:
        res += (-1)**(cur_iteration/2)*cur_number
        cur_iteration += 2
        cur_number *= x2/(cur_iteration-1)/cur_iteration

    return res


eps = float(input())
x = float(input())
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))
