#https://codeforces.com/problemset/problem/1475/A

t = int(input())

for i in range(t):
    temp = int(input())
    while temp % 2 == 0:
        temp //= 2
    if temp == 1:
        print("NO")
    else:
        print("YES")