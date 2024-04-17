# https://codeforces.com/problemset/problem/1669/A

t = int(input())
for _ in range(t):
    temp = int(input())
    if temp <= 1399:
        print("Division 4")
    elif temp <= 1599:
        print("Division 3")
    elif temp <= 1899:
        print("Division 2")
    else:
        print("Division 1")
