a = list(map(int, input().split("+")))
b = []
count = 1
res = ''

while len(a) != len(b):
    for i in range(len(a)):
        if a[i] == count:
            b.append(a[i])
        else:
            continue
    count += 1

for i in b:
    res += str(i)

print("+".join(res))