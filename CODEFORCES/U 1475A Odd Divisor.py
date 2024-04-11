#https://codeforces.com/problemset/problem/1475/A

import math

def is_prime(n):
    if n <= 1:
        a = False
    elif n >= 2:
        a = True
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0:
                a = False
                break
    return a

def next_prime(n):
    result = n + 1
    while True:
        if is_prime(result):
            break
        else:
            result += 1
    return result

t = int(input())
test_cases = []
odd = 3

for i in range(t):
    temp = int(input())
    test_cases.append(temp)

for i in test_cases:
    if i % 2 == 1:
        print("YES")
    else:
        flag = False
        while odd * odd <= i:
            if i % odd == 0:
                flag = True
                break
            else:
                odd = next_prime(odd)
        if flag:
            print("YES")
        else:
            print("NO")
