# https://codeforces.com/problemset/problem/155/A

n = int(input())
scores = list(map(int, input().split()))
max = scores[0]
min = scores[0]
count = 0
for i in range(1, n):
    if scores[i] > max:
        count += 1
        max = scores[i]
    elif scores[i] < min:
        count += 1
        min = scores[i]

print(count)
