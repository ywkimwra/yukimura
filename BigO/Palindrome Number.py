def is_palindrome(x):
    return str(x) == str(x)[::-1]


nums = []

while True:
    num = int(input())
    if num == -1:
        break
    nums.append(num)

for i in range(len(nums)):
    if is_palindrome(nums[i]):
        print(i, end=" ")
