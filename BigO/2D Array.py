#BT1

# nrows, ncols = map(int, input().split())
# a = []
# sum = 0

# for i in range(nrows):
#     temp = list(map(int, input().split()))
#     a.append(temp)

# for i in range(nrows):
#     sum = 0
#     for j in range(ncols):
#         sum += a[i][j]
#     print(sum, end=" ")

#BT2

nrows, ncols = map(int, input().split())
a = []

for i in range(nrows):
    temp = list(map(int, input().split()))
    a.append(temp)

for j in range(ncols):
    all_negative = True
    for i in range(nrows):
        if a[i][j] >= 0:
            all_negative = False
            break
    if all_negative:
        print(j + 1)