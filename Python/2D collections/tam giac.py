n = 10

# for i in range(n):
#     for j in range(n - i):
#         print(" ", end = "")
#     for j in range(2 * i + 1):
#         print("*", end = "")
#     print()
#
# for i in range(n):
#     for j in range(n - (i + 1)):
#         print(" ", end = "")
#     for j in range(i + 1):
#         print("*", end = " ")
#     print()
#
#
# for i in range(n):
#     print((n-i-1)*" ", end="")
#     if i == 0:
#         print("*")
#     elif i < n-1:
#         print("*", end="")
#         print((2*i-1)*" ", end="")
#         print("*")
#     else:
#         print(n*"* ")
#
# for row in range(6):
#     for col in range(7):
#         if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row == 2 and col % 6 == 0) or (row == 3 and col == 1) or (row == 3 and col == 5) or (row == 4 and (col == 2 or col == 4)) or (row == 5 and col == 3):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#
# if n % 2 == 0:
#     for i in range(int(n/2)):
#         print("*" * (i + 1), end="")
#         print(" " * (n - (i * 2) - 2), end="")
#         print("*" * (i + 1))
#     for j in range(int(n/2), n):
#         print("*" * (n - j), end="")
#         print(" " * ((int(n/2) + j - n) * 2), end="")
#         print("*" * (n - j))
# else:
#     for i in range(int(n//2)):
#         print("*" * (i + 1), end="")
#         print(" " * (n - (i * 2) - 2), end="")
#         print("*" * (i + 1))
#     print("*" * n)
#     for j in range(int(n//2) + 1, n):
#         print("*" * (n - j), end="")
#         print(" " * ((int(n//2) + j - n) * 2 + 1), end="")
#         print("*" * (n - j))

for i in range(int(n//2)):
    print("*" * (i + 1), end="")
    print(" " * (n - (i * 2) - 2), end="")
    print("*" * (i + 1))
print("*" * n)
for j in range(int(n//2) + 1, n):
    print("*" * (n - j), end="")
    print(" " * (((int(n//2) + j - n) * 2) + (n % 2)), end="")
    print("*" * (n - j))