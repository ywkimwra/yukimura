# https://codeforces.com/problemset/problem/230/B

def is_t_prime(num: int) -> str:
    count = 0
    for _ in range(2, num + 1):
        if num % _ == 0:
            count += 1

    if count == 3:
        return "YES"
    else:
        return "NO"


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    for _ in nums:
        print(is_t_prime(_))


if __name__ == "__main__":
    main()
