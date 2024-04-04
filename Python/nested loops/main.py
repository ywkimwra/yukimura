for x in range(1, 10):
   print(x, end="")


rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter the symbol to use: ")


for x in range(rows):
    for x in range(columns):
        print(symbol, end="")
    print()


for x in range(3):
    for x in range(1, 6):
        print(x, end="")
    print()