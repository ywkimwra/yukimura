# n = int(input())
# a = list(map(int, input().split()))

# import math

# def is_prime(n):
#     if n <= 1:
#         a = False
#     elif n >= 2:
#         a = True
#         for i in range(2, round(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 a = False
#                 break
#     return a
# a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# ans = 0
# like = True
# count = 0

# for i in range(n):
#     ans += a[i]

#     if a[i] >= ans:
#         ans = a[i]

#     if a[i] % 2 == 0:
#         print(a[i])

#     if a[i] == 0:
#         like = False
#         break

#     if is_prime(a[i]):
#         print(a[i])

# print(like)
# print(ans)

# print(a[1:3])

# def inc(l):
#     for i in range(len(l)):
#         l[i] *= 2

# lst = [10, 20, 30]

# for x in lst:
#     print(x, end=" ")

# inc(lst)

# for x in lst:
#     print(x, end=""

# male = 0
# female = 0

# for i in range(n):
#     if a[i] == 0:
#         male += 1
#     else:
#         female += 1

# if male == female:
#     print("YES")
# else:
#     print("NO")


# id = 1
# for i in range(n):
#     if id in a:
#         id += 1
#     else:
#         break
# print(id)

n = int(input())
max_tao = 0
max_cam = 0
index = -1
for i in range(n):
    tao, cam = list(map(int, input().split()))
    if tao > max_tao:
        max_tao = tao
        max_cam = cam
        index = i
    elif tao == max_tao and cam > max_cam:
        max_cam = cam
        index = i
index += 1
print(index)