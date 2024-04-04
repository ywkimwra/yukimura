x = int(input())
 
if x % 5 == 0:
    step = x / 5
else:
    step = (x // 5) + 1
 
print(int(step))