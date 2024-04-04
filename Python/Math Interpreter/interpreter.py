expression = input("expression: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
    a = x + z
elif y == "-":
    a = x - z
elif y == "/" and z != 0:
    a = x / z
elif y == "*":
    a = x * z

result = round(a, 1)

print(result)
