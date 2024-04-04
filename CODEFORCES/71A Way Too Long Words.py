n = int(input())

for i in range(n):
    word = input()
    if len(word) > 10:
        # print(word[0], end="")
        # print(str(len(word)-2), end="")
        # print(word[-1])
        print(f"{word[0]}{str(len(word) - 2)}{word[-1]}")
    else:
        print(word)
