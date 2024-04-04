#name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")

#result = len(name)
#result = name.find("H")
#result = name.rfind("h")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isalpha() #False if contain any spaces
#result = name.isdigit()

#result = phone_number.count("-")
#phone_number = phone_number.replace("-", "")

#print(phone_number)

#print(help(str))

#validate user input exersise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username :")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"WELCOME {username.upper()}")