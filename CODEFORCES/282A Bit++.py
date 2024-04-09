#https://codeforces.com/problemset/problem/282/A

n = int(input())
commands = []
result = 0

for i in range(n):
    temp = input()
    commands.append(temp)

for i in commands:
    if i[:2] == "++" or i[1:] == "++":
        result += 1
    elif i[:2] == "--" or i[1:] == "--":
        result -= 1
    
print(result)