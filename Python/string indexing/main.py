#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "4700-1235-5476-2334"

print(credit_number[0])
print(credit_number[:4])

print(credit_number[5:9])
print(credit_number[5:])

print(credit_number[-1])
print(credit_number[::2])

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1]
print(credit_number)