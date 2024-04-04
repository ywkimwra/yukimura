n = int(input("Enter n: "))
count = 0

for i in range(1, n + 1):
    a = ((1 + i) * i) / 2
    if n - a < 0:
        break
    else:
        n -= a
        count += 1

print(count)