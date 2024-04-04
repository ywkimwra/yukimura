word = input()

for i in range(len(word)):
    if i == 0:
        word = word.replace(word, word.upper())

print(word)