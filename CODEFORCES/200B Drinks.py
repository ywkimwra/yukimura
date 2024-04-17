# https://codeforces.com/problemset/problem/200/B

n = int(input())
p = list(map(int, input().split()))
v = 0

for _ in p:
    v += _

print(v / n)
