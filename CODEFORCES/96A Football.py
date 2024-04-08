n = int(input())
count_1 = 0
count_0 = 0
flag = True

for i in range(len(str(n))):
    if i == 1:
        count_1 += 1
        if count_1 > 7:
            print("YES")
            flag = False
            break
    else:
        count_1 = 0

for j in range(len(str(n))):
    if j == 0:
        count_0 += 1
        if count_0 > 7:
            print("YES")
            flag = False
            break
    else:
        count_0 = 0

if flag:
    print("NO")