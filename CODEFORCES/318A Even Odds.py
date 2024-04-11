n, k = map(int, input().split())
num = []

for i in range(n):
    if (i + 1) % 2 == 1:
        num.append(i + 1)

for i in range(n):
    if (i + 1) % 2 == 0:
        num.append(i + 1)

print(num[k-1])