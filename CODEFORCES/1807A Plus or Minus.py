# https://codeforces.com/problemset/problem/1807/A

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    if a + b == c:
        print("+")
    else:
        print("-")