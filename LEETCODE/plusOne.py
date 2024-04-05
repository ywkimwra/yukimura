digits = [1, 2, 4, 8, 5]
num = ""
new_digits = []

for digit in digits:
    num += str(digit)

new_num = int(num) + 1

# print(new_num)

for i in range(len(str(new_num))):
    new_digits.append(str(new_num)[i])

