#BT1

# a = ["b", "i", "g", "o"]
# n = input()

# for i in n:
#     if i.lower() in a:
#         print("yes")
#     else:
#         print("no")

#BT2

# n = input()
# count = 0

# for i in n:
#     if ord("0") <= ord(i) <= ord("9"):
#         count += 1

# print(count)

#BT3

# def remodel_string(string):
#     # Remove leading and trailing spaces
#     while string[0] == ' ':
#         string = string[1:]

#     while string[-1] == ' ':
#         string = string[:-1]

#     # Replace multiple spaces with a single space
#     remodeled_string = ''
#     prev_char = ''
#     for char in string:
#         if char == ' ' and prev_char == ' ':
#             continue
#         remodeled_string += char
#         prev_char = char

#     return remodeled_string

# print(remodel_string(input()))

#BT4

# n = int(input())
# names = []

# for i in range(n):
#     name = input()
#     names.append(name)

# for name in names:
#     remodeled_string = ""
#     capitalize_next = True

#     for char in name:
#         if char.isalpha():
#             if capitalize_next:
#                 remodeled_string += char.upper()
#                 capitalize_next = False
#             else:
#                 remodeled_string += char.lower()
#         elif char.isspace():
#             capitalize_next = True
#             remodeled_string += char

#     print(remodeled_string)

#BT8

# string = input().split()

# for i in range(len(string), 0, -1):
#     print(string[i-1], end=" ")

#BT7

# string = input()
# capitalize_next = False
# res = ""

# for i in range(len(string)):
#     if capitalize_next and string[i].isalpha():
#         res += string[i].upper()
#         capitalize_next = False
#     else:
#         res += string[i]
#         if string[i:i+2] == ". ":
#             capitalize_next = True

# print(res)

#BT6

# string = input()
# alpha = []

# for i in string:
#     while i not in alpha and i != " ":
#         alpha.append(i)
#         string = string[1:]

# print(alpha)
# print(len(alpha))

#BT 5

n = int(input())
strings = []
for i in range(n):
    string = input().upper()
    strings.append(string)

for string in strings:
    for i in string:
        char_count = {}
        if i not in char_count:
            char_count[i] = 0
        char_count[i] += 1

print(char_count)