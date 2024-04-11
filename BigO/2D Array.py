# BT1 sum rows

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
#         print(j)

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

# nrows, ncols = map(int, input().split())
# a = []
# evens = []
# count = 0
# for i in range(nrows):
#     temp = list(map(int, input().split()))
#     a.append(temp)

# for i in range(nrows):
#     count = 0
#     for j in range(ncols):
#         if a[i][j] % 2 == 0:
#             count += 1
#     evens.append(count)

# max_index = 0
# for i in range(len(evens)):
#     if evens[i] > evens[max_index]:
#         max_index = i
# print(max_index)

# nrows, ncols = map(int, input().split())
# a = []

# for i in range(nrows):
#     temp = list(map(int, input().split()))
#     a.append(temp)

# count = 0

# for i in range(nrows):
#     for j in range(ncols):
#         if a[i][j] > 100:
#             count += 1

# print(count)

# nrows, ncols = map(int, input().split())
# a = []
# count = 0

# for i in range(nrows):
#     temp = list(map(int, input().split()))
#     a.append(temp)

# for i in range(nrows):
#     for j in range(ncols):
#         value = a[i][j]
#         is_saddle = True

#         for x in range(ncols):
#             if value < a[i][x]:
#                 is_saddle = False
#                 break
        
#         if is_saddle:
#             for y in range(nrows):
#                 if value > a[y][j]:
#                     is_saddle = False
#                     break
#         if is_saddle:
#             count += 1

# print(count)

<<<<<<< HEAD
# nrows, ncols = map(int, input().split())
# a, b, p = map(int, input().split())
# matrix = []

# for i in range(nrows * ncols):
#     if i == 0:
#         matrix.append(a)
#     elif i == 1: 
#         matrix.append(b)
#     else:
#         c = (a + b) % p
#         a = b
#         b = c
#         matrix.append(b)

# for i in range(nrows):
#     for j in range(ncols):
#         index = i * ncols + j
#         print(matrix[index], end=" ")
#     print()

# n = int(input())
# matrix = []
# max_value = 0
# is_queen = True

# for i in range(n):
#     temp = list(map(int, input().split()))
#     matrix.append(temp)

# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] > max_value:
#             max_value = matrix[i][j]

# M, N = map(int, input().split())  # Nhập số dòng và số cột của ma trận
# a, b, p = map(int, input().split())  # Nhập giá trị đầu tiên a, b và số p

# matrix = [[0 for _ in range(N)] for _ in range(M)]  # Khởi tạo ma trận với giá trị ban đầu là 0

# # Gán giá trị cho 2 ô đầu tiên
# matrix[0][0] = a
# matrix[0][1] = b

# # Tính toán và gán giá trị cho từng ô trong ma trận
# for i in range(M):
#     for j in range(N):
#         if i == 0 and (j == 0 or j == 1):
#             continue  # Bỏ qua 2 ô đầu tiên đã được gán giá trị trước đó
#         if j < 2:
#             matrix[i][j] = (matrix[i-1][j] + matrix[i][j-1]) % p
#         else:
#             matrix[i][j] = (matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-2]) % p

# # In ma trận
# for row in matrix:
#     print(" ".join(str(x) for x in row))

=======
>>>>>>> 24a0cd86e3956ca25222a3536f79aa4544df9de1
n = int(input())
matrix = []
count = 0

for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

for i in range(n):
    for j in range(n):
        value = matrix[i][j]
        is_queen = True

        for x in range(n):
            if value < matrix[i][x]:
                is_queen = False
                break
        
        if is_queen:
            for y in range(n):
                if value < matrix[y][j]:
                    is_queen = False
                    break

        if is_queen:
            for x in range(n):
                y = x - j + i
                if (y != i or x != j) and (0 <= y <= (n-1)):
                    if value < matrix[y][x]:
                        is_queen = False
                        break
                y = j - x + i
                if (y != i or x != j) and (0 <= y <= (n-1)):
                    if value < matrix[y][x]:
                        is_queen = False
                        break

        if is_queen:
            count += 1

print(count)