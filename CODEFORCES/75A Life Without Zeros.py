a = int(input())
b = int(input())

c = a + b

x = int(str(a).replace("0", ""))
y = int(str(b).replace("0", ""))
z = int(str(c).replace("0", ""))

if z == x + y:
    print("YES")
else:
    print("NO")