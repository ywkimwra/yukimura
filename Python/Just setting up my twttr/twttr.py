text = input("Enter your text: ").lstrip()
vowels = {"a", "o", "e", "u", "i"}
for i in text:
    if i.lower() in vowels:
        text = text.replace(i, "")

print(f"Output: {text}")

x = "le chi huy"

print(x[::-1])