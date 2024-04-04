row = []

for i in range(5):
    row.append(list(map(int, input().split(" "))))
    
# print(row)

position = []
for i in range(5):
    for j in range(5):
        if row[i][j] == 1:
            position.append((i, j)) # position = [i, j]
            break

# print(position)
# print(position[0][0])
# print(position[0][1])

move = abs(position[0][0] - 2) + abs(position[0][1] - 2)
print(move)