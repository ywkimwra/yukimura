n, m, a = map(int, input().split())
 
if n % a == 0:
    i = int(n / a)
else:
    i = int(n // a) + 1
    
if m % a == 0:
    j = int(m / a)
else:
    j = int(m // a) + 1
 
x = i * j
print(x)