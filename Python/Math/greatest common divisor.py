from isPrime import is_prime

a = int(input())

for i in range(a):
    if is_prime(i):
        a = a // i
        print(a)

# print("**********************")
# for j in range(b):
#     if is_prime(j):
#         print(j, end="")

# def gcd():
# def main():
