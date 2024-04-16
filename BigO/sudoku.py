sudoku = []
is_valid = True

for i in range(9):
    temp = list(map(int, input().split()))
    sudoku.append(temp)

for i in range(9):
    row = set()
    for j in range(9):
        if sudoku[i][j] in row:
            is_valid = False
            break
        elif sudoku[i][j] != 0:
            row.add(sudoku[i][j])

for j in range(9):
    col = set()
    for i in range(9):
        if sudoku[i][j] in col:
            is_valid = False
            break
        elif sudoku[i][j] != 0:
            col.add(sudoku[i][j])

for block in range(9):
        block_set = set()
        for i in range((block // 3) * 3, (block // 3) * 3 + 3):
            for j in range((block % 3) * 3, (block % 3) * 3 + 3):
                if sudoku[i][j] in block_set:
                    is_valid = False
                    break
                if sudoku[i][j] != 0:
                    block_set.add(sudoku[i][j])

if is_valid:
    print("YES")
else:
    print("NO")