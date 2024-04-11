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

n = input()

print(n.title())