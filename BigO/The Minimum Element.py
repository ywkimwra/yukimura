arr = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr.append(n)

min = arr[0]

for i in range(1, len(arr)):
    if arr[i] < min:
        min = arr[i]

print(min)