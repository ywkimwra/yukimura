arr = []

while True:
    n = int(input())
    if n == 0:
        break
    arr.append(n)

for i in range(len(arr)):
    print(i + 1, end=" ")
    print(arr[i], end=" ")