#https://codeforces.com/problemset/problem/236/A

string = input().lower()
alphabet = []
for i in string:
    if i not in alphabet:
        alphabet.append(i)
    else:
        continue

if len(alphabet) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
