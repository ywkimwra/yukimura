#https://codeforces.com/problemset/problem/1475/A

t = int(input())
test_cases = []
odd = 3
flag = True

for i in range(t):
    temp = int(input())
    test_cases.append(temp)

for i in test_cases:
    while flag:
        if i // odd < 1:
            print("NO")
        elif i // odd >= 1:
            