vowels = ["a", "o", "y", "e", "u", "i"]

n = input()
n = n.lower()

for i in vowels:
    n = n.replace(i, "")
result = ".".join(n)

print("." + result)