import statistics as st

x = [int(x) for x in input().split()]
x = [i for i in x if i > st.mean(x)]

for i in x:
    print(i, end=" ")
