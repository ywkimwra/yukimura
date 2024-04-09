n = int(input())
cache = {}

def fib_loop(n):
    n0 = 0
    n1 = 1
    if n <= 0:
        return 0
    elif n == 1:
        return n0
    elif n == 2:
        return n1
    for i in range(2, n):
        sum = n0 + n1
        n0 = n1
        n1 = sum
    return n1

def fib_recur(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)
    
def fib_memoization(n, cache):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n not in cache:
        cache[n] = fib_memoization(n-1, cache) + fib_memoization(n-2, cache)
    return cache[n]

print(fib_memoization(n, cache))