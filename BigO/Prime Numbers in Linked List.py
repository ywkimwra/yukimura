import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


nums = []

while True:
    x = int(input())
    if x == -1:
        break
    nums.append(x)

count = 0

for num in nums:
    if is_prime(num):
        count += 1

print(count)
