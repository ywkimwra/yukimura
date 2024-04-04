m, n = map(int, input().split())

if m % 2 == 0:
    a = (m / 2) * n
else:
    b = (m // 2) * n
    a = (n // 2) + b

print(int(a))