N = int(input())
adjacent_matrix = []

for _ in range(N):
    row = list(map(int, input().split()))
    adjacent_matrix.append(row)

flag = True

for i in range(N):
    for j in range(i + 1, N):
        if adjacent_matrix[i][j] != adjacent_matrix[j][i]:
            flag = False
            break

print("YES" if flag else "NO")