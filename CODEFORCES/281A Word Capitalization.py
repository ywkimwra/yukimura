word = input()

for i in range(len(word)):
    if i == 0:
        word[i] = word[i].replace(word[i], word.upper())

print(word)