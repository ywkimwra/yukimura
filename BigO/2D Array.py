nrows, ncols = map(int, input().split())
a = []
sum = 0

for i in range(nrows):
    temp = map(int, input().split())
    a.append(temp)

for i in range(nrows):
    for j in range(ncols):
        print(a[i][j], end= " ")
    print()