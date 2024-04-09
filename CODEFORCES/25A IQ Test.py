n = int(input())
a = list(map(int, input().split()))
last_even = 0
last_odd = 0
even_counter = 0
odd_counter = 0

for i in range(n):
    if a[i] % 2 == 0:
        even_counter += 1
        last_even = i
        odd_counter -= 1
    else:
        odd_counter += 1
        last_odd = i
        even_counter -= 1

if even_counter > 0:
    print(last_odd + 1)
else:
    print(last_even + 1)