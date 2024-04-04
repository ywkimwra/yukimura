import math

def is_prime(n):
    if n <= 1:
        a = False
    elif n >= 2:
        a = True
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0:
                a = False
                break
    return a

def main():
    n = int(input())
    for i in range(n):
        if is_prime(i):
            print(i)
    return

if __name__ == "__main__":
    main()