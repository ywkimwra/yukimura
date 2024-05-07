import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


N = int(input())
A = list(map(int, input().split()))

primes = []
non_primes = []

for num in A:
    if is_prime(num):
        primes.append(num)
    else:
        non_primes.append(num)

non_primes = merge_sort(non_primes)

result = []
prime_index = 0
non_prime_index = 0

for num in A:
    if is_prime(num):
        result.append(primes[prime_index])
        prime_index += 1
    else:
        result.append(non_primes[non_prime_index])
        non_prime_index += 1

print(*result)
