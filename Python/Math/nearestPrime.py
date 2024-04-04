from isPrime import is_prime

def main():
    n = int(input())
    minus_one = n
    plus_one = n
    result = 0

    while True:
        flag1 = is_prime(minus_one)
        if flag1:
            result = minus_one
            break
        else:
            minus_one -= 1

        flag2 = is_prime(plus_one)
        if flag2:
            result = plus_one
            break
        else:
            plus_one += 1
    print(result)
    return

if __name__ == "__main__":
    main()
