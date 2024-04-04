email = input("Enter your email: ")

#lchuy97@gmail.com

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")