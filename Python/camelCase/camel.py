name = input("camelCase: ").lstrip()

for i in name:
    if i.isupper():
        name = name.replace(i, f"_{i.lower()}")

print(f"snake_case: {name}")