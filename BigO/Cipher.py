string = input()

odd = ""
even = ""

for i in range(len(string)):
    if i % 2 == 1:
        odd += string[i]
        even += "_"
    else:
        odd += "_"
        even += string[i]

reverse_even = ""

for i in range(len(even) - 1, -1, -1):
    reverse_even += even[i]

result = ""

for i in range(len(string)):
    if i % 2 == 1:
        result += odd[i]
    else:
        result += reverse_even[i]

print(result)