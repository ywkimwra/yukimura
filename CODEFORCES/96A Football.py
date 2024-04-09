n = input()
zero_counter = 0
one_counter = 0

for i in n:
    if i == "1":
        one_counter += 1
        zero_counter = 0
        if one_counter >= 7:
            break
    else:
        zero_counter += 1
        one_counter = 0
        if zero_counter >= 7:
            break

if zero_counter >= 7 or one_counter >= 7:
    print("YES")
else:
    print("NO")