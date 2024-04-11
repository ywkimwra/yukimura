#https://codeforces.com/problemset/problem/734/A

n = int(input())
scoreboard = input()

A_counter = 0
D_counter = 0

for i in range(n):
    if scoreboard[i] == "A":
        A_counter += 1
    else:
        D_counter += 1

if A_counter > D_counter:
    print("Anton")
elif D_counter > A_counter:
    print("Danik")
else:
    print("Friendship")