n = int(input())
a = list(map(int, input().split()))

fact = True
for i in range(n):
    if a[i] == 1:
        fact = False
        break

if fact:
    print("EASY")
else:
    print("HARD")