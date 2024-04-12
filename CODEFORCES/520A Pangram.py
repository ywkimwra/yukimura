#https://codeforces.com/problemset/problem/520/A

n = int(input())
string = input().lower()
alphabet = []

for i in range(n):
    if string[i] not in alphabet:
        alphabet.append(string[i])
    else:
        continue

if len(alphabet) == 26:
    print("YES")
else:
    print("NO")
