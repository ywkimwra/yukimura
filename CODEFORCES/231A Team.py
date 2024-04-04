n = int(input())
contest = 0
for i in range(n):
    Petya, Vasya, Tonya = map(int, input().split(" "))
    if Petya + Vasya + Tonya >= 2:
        contest += 1
print(contest)
