a = [int(x) for x in input().split()][1:]
b = [int(x) for x in input().split()][1:]

first = 1

pr=[]

for i in a:
    if i not in b and i not in pr:
        if first == 0:
            print(" ",end="")
        else:
            first = 0
        print(i,end="")
        pr.append(i)
for i in b:
    if i not in a and i not in pr:
        if first == 0:
            print(" ",end="")
        else:
            first = 0
        print(i,end="")
        pr.append(i)
