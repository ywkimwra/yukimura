n = int(input())
tram = 0
max = 0

for i in range(n):
    exit, enter = map(int, input().split())
    tram -= exit
    tram += enter
    if tram > max:
        max = tram
print(max)