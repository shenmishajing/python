import math


def prime(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i) == 0:
            return 0

    return 1


number = 10
letter = 0
blank = 0
digit = 0
other = 0

while 1:
    s = input()
    for c in s:
        number -= 1
        if number < 0:
            break
        if c.isalpha():
            letter += 1
        elif c.isspace():
            blank += 1
        elif c.isdigit():
            digit += 1
        else:
            other += 1
    if number <= 0:
        break
    else:
        number-=1
        blank+=1
        if number <= 0:
            break


print("letter = %d, blank = %d, digit = %d, other = %d" % (letter, blank, digit, other))
