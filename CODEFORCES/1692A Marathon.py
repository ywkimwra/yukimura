t = int(input())

for i in range(t):
    a, b, c, d = map(int, input().split())
    count = 0
    flag = True
    while flag:
        if b > a:
            count += 1
        elif c > a:
            count += 1
        elif d > a:
            count += 1
        else:
            flag = False
    print(count)
