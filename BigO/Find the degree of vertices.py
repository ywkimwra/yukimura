N, X = map(int, input().split())
adjacent_matrix = []

for _ in range(N):
    row = list(map(int, input().split()))
    adjacent_matrix.append(row)

degree = 0
for j in range(N):
    if adjacent_matrix[X][j] == 1:
        degree += 1

print(degree)
