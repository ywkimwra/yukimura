def print_odd(n: int) -> int:
    return 2 * n - 1

def print_even(n: int) -> int:
    return 2 * n

def main():
    n, k = map(int, input().split())

    if k <= (n // 2 + n % 2):
        print(print_odd(k))
    else:
        j = k - (n // 2) - (n % 2)
        print(print_even(j))

if __name__ == "__main__":
    main()