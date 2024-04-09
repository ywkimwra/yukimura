#BT1 sum rows

# nrows, ncols = map(int, input().split())
# a = []
# sum = 0

# for i in range(nrows):
#     temp = list(map(int, input().split()))
#     a.append(temp)

# for i in range(nrows):
#     sum = 0
#     for j in range(ncols):
#         sum += a[i][j]
#     print(sum, end=" ")

#BT2 print col which all negative number

# nrows, ncols = map(int, input().split())
# a = []

# for i in range(nrows):
#     temp = list(map(int, input().split()))
#     a.append(temp)

# for j in range(ncols):
#     all_negative = True
#     for i in range(nrows):
#         if a[i][j] >= 0:
#             all_negative = False
#             break
#     if all_negative:
#         print(j + 1)

#BT3 check prime number on the fence of 2d array

# nrows, ncols = map(int, input().split())
# a = []
# prime_num = []
# count = 0

# for i in range(nrows):
#     temp = list(map(int, input().split()))
#     a.append(temp)

# def is_prime(n):
#     if n <= 1:
#         a = False
#     elif n >= 2:
#         a = True
#         for i in range(2, n):
#             if n % i == 0:
#                 a = False
#                 break
#     return a

# for i in range(nrows):
#     for j in range(ncols):
#         if j == 0 or j == (ncols - 1) or i == 0 or i == (nrows - 1):
#             if is_prime(a[i][j]):
#                 count += 1
#                 prime_num.append(a[i][j])

# print(count)
# print(prime_num)

#BT4 check prime on X of 2d sq array

# nrows, ncols = map(int, input().split())
# a = []
# prime_num = []
# count = 0

# for i in range(nrows):
#     temp = list(map(int, input().split()))
#     a.append(temp)

# def is_prime(n):
#     if n <= 1:
#         a = False
#     elif n >= 2:
#         a = True
#         for i in range(2, n):
#             if n % i == 0:
#                 a = False
#                 break
#     return a

# for i in range(nrows):
#     for j in range(ncols):
#         if i == j or j == (nrows - 1 - i):
#             if is_prime(a[i][j]):
#                 count += 1
#                 prime_num.append(a[i][j])

# print(count)
# print(prime_num)

#BT5 prime product on the extra diagonal

# n = int(input())
# a = []
# result = 1
# prime_num = []

# def is_prime(n):
#     if n <= 1:
#         a = False
#     elif n >= 2:
#         a = True
#         for i in range(2, n):
#             if n % i == 0:
#                 a = False
#                 break
#     return a

# for i in range(n):
#     temp = list(map(int, input().split()))
#     a.append(temp)

# for i in range(n):
#     for j in range(n):
#         if j == (n - 1 - i):
#             if is_prime(a[i][j]):
#                 result *= a[i][j]
#                 prime_num.append(a[i][j])

# if len(prime_num) == 0:
#     result = 0

# print(result)