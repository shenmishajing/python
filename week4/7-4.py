c = input()
s = input()

i = s.rfind(c)
if i == -1:
    print("Not Found")
else:
    print("index =", i)
