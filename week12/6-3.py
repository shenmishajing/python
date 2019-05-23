def CountDigit(number, digit):
    number = str(number)
    count = number.count(str(digit))
    return count


/* 请在这里填写答案 * /

number, digit = input().split()
number = int(number)
digit = int(digit)
count = CountDigit(number, digit)
print("Number of digit 2 in "+str(number)+":", count)
