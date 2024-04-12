#https://codeforces.com/problemset/problem/677/A

n, h = map(int, input().split())
count = 0
a = list(map(int, input().split()))

for i in range(n):
    if a[i] <= h:
        count += 1
    else:
        count += 2

print(count)