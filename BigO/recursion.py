import sys

sys.setrecursionlimit(10000)

n = int(input())
a = list(map(int, input().split()))

#
def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)
#
def ulln(n):
    if n % 2 == 1:
        return n
    return ulln(n / 2)
#
def count_digits(n):
    if n < 10:
        return 1
    return count_digits(n // 10) + 1
#
def first_digit(n):
    if n < 10:
        return n
    return first_digit(n // 10)
#
def largest_digit(n):
    if n < 10:
        return n
    
    a = largest_digit(n // 10)
    b = n % 10

    return max(a, b)
#
def sum_of_even(a, n):
    if n == 0:
        return 0
    
    if a[n - 1] % 2 == 0:
        return a[n - 1] + sum_of_even(a, n - 1)
    else:
        return sum_of_even(a, n - 1)
#
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, (n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#
def first_prime(a, n):
    if n >= len(a):
        return -1
    if is_prime(a[n]):
        return n
    return first_prime(a, n + 1)
#
def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

a, b = map(int, input().split())

gcd = gcd_recursive(a, b)

print(gcd)
#
def sum_of_even(a, n):
    if n == 0:
        return 0
    
    if a[n - 1] % 2 == 0:
        return a[n - 1] + sum_of_even(a, n - 1)
    else:
        return sum_of_even(a, n - 1)
      
print(sum_of_even(a, n))
#
def largest_digit(n):
    if n < 10:
        return n
    
    a = largest_digit(n // 10)
    b = n % 10

    return max(a, b)

print(largest_digit(abs(n)))
#
def decimal_to_binary_recursive(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return decimal_to_binary_recursive(n // 2) + str(n % 2)

n = int(input())

binary = decimal_to_binary_recursive(n)

print(binary)
#
def decimal_to_hexadecimal_recursive(n):
    if n < 10:
        return str(n)
    elif n == 10:
        return 'A'
    elif n == 11:
        return 'B'
    elif n == 12:
        return 'C'
    elif n == 13:
        return 'D'
    elif n == 14:
        return 'E'
    elif n == 15:
        return 'F'
    else:
        return decimal_to_hexadecimal_recursive(n // 16) + decimal_to_hexadecimal_recursive(n % 16)

n = int(input())

hexadecimal = decimal_to_hexadecimal_recursive(n)

print(hexadecimal)