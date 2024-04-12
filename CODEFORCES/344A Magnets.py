#https://codeforces.com/problemset/problem/344/A

n = int(input())
a = []
prev_magnet = ""
count = 0
for i in range(n):
    temp = input()
    a.append(temp)

for i in range(n):
    if a[i] != prev_magnet:
        count += 1
        prev_magnet = a[i]
    else:
        prev_magnet = a[i]

print(count)