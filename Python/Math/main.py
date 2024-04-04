# # ARITHMETIC OPERATORS

# friends = 10
# friends =friends + 1
# friends += 1

# friends = friends - 2
# friends -= 2

# friends = friends * 3
# friends *= 3

# friends = friends / 2
# friends /= 2

# friends = friends ** 3
# friends **= 3

# remainder = friends % 3

# print(friends)
# print(remainder)

# # MATH FUNCTIONS

# x = 3.14
# y = -4
# z = 2

# result = round(x)
# result = abs(y)
# result = pow(2, 8)
# result = max(x, y, z)
# result = min(x, y, z)
# print(result)

# import math

# x = 12.9
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x) #round up
# result = math.floor(x) #round down
# print(result)

# # EXERCISES

# import math

# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# area = math.pi * pow(radius, 2)

# print(f"The circumference is: {round(circumference, 2)}cm")
# print(f"The area of the circle is: {round(area, 2)}cm^2")

# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))

# c = math.sqrt(pow(a, 2) + pow(b, 2))

# print(f"Side C = {c}")

# def main():
#     n = int(input())
#     sum = 0
#     for i in range(n+1):
#         sum += (i * i)
#     print(sum)
#     return

# if __name__ == "__main__":
#     main()

# a, b = map(int, input().split())

# def gcd(a, b):
#     r = a % b
#     while r != 0:
#         a = b
#         b = r
#         r = a % b
#     return b

# c = a / gcd(a, b)
# d = b / gcd(a, b)

# print(f"{c} {d}")

n = int(input())
def count_degit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    print(count)
    return

count_degit(n)