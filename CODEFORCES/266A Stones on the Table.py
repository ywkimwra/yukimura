#https://codeforces.com/problemset/problem/266/A

n = int(input())
stones = input()
prev_stone = ""
count = 0
for stone in stones:
    if stone == prev_stone:
        count += 1
    else:
        prev_stone = stone
    
print(count)