n = int(input())

st = []

for i in range(n):
    s, name = input().split()
    st.append((s, name))

output = []

num = 0
while num < n:
    cur = 0
    while st[cur] in output:
        cur += 1
    s, name = st[cur]
    cur = len(st)-1
    while st[cur] in output or st[cur][0] == s:
        cur -= 1
    print(name, st[cur][1])
    output.append((s, name))
    output.append(st[cur])
    num += 2
