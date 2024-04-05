n = int(input())
a = list(map(int, input().split()))

less = []
greater = []
zero = []

for i in a:
    if i > 0:        
        greater.append(i)
    elif i < 0:
        less.append(i)
    else:
        zero.append(i)

if len(less) % 2 == 0:
    zero.append(less[-1])
    less = less[:-1]

if len(greater) == 0:
    count = -1
    while len(greater) < 2:
        greater.append(less[count])
        less = less[:-1]

print(len(less), end=" ")
for x in range(len(less)):
    print(less[x], end=" ")
print()
print(len(greater), end=" ")
for y in range(len(greater)):
    print(greater[y], end=" ")
print()
print(len(zero), end=" ")
for z in range(len(zero)):
    print(zero[z], end=" ")