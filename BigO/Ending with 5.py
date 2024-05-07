N = int(input())
nums = []

for i in range(N):
    num = int(input())
    nums.append(num)

nums_updated = []

for num in nums:
    if num % 10 != 5:
        nums_updated.append(num)

print(*nums_updated)
