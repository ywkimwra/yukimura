#https://codeforces.com/problemset/problem/1475/A

t = int(input())
test_cases = []

for i in range(t):
    temp = int(input())
    while temp % 2 == 0 and temp > 2:
        temp //= 2
    test_cases.append(temp)

for i in test_cases:
    if i % 2 == 1:
        print("YES")
    else:
        flag = False
        odd = 3
        while i >= odd:
            if i % odd == 0:
                flag = True
                break
            else:
                odd += 2

        if flag:
            print("YES")
        else:
            print("NO")