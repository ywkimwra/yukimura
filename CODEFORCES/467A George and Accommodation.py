#https://codeforces.com/problemset/problem/467/A

n = int(input())
rooms = []
count = 0
for i in range(n):
    temp = list(map(int, input().split()))
    rooms.append(temp)

for i in range(n):
    if rooms[i][1] - rooms[i][0] >= 2:
        count += 1

print(count)