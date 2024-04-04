n = int(input())
a = list(map(int, input().split()))

import math

def is_prime(n):
    if n <= 1:
        a = False
    elif n >= 2:
        a = True
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0:
                a = False
                break
    return a
a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
ans = 0
like = True
count = 0

for i in range(n):
    ans += a[i]

    if a[i] >= ans:
        ans = a[i]

    if a[i] % 2 == 0:
        print(a[i])

    if a[i] == 0:
        like = False
        break

    if is_prime(a[i]):
        print(a[i])

print(like)
print(ans)

print(a[1:3])

def inc(l):
    for i in range(len(l)):
        l[i] *= 2

lst = [10, 20, 30]

for x in lst:
    print(x, end=" ")

inc(lst)

for x in lst:
    print(x, end="")