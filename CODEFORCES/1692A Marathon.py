t = int(input())
test_cases = []

for i in range(t):
    a, b, c, d = list(map(int, input().split()))
    test_cases.append([a, b, c, d])

for j in range(t):
    count = 0
    for k in range(1, 4):
        if test_cases[j][k] > test_cases[j][0]:
            count += 1
    print(count)
