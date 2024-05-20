class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


N = int(input())
adjacent_matrix = []

for _ in range(N):
    row = list(map(int, input().split()))
    adjacent_matrix.append(row)

edge_list = []

for i in range(N):
    for j in range(N):
        if adjacent_matrix[i][j] == 1:
            edge_list.append((i, j))

print(len(edge_list))
for edge in edge_list:
    print(*edge)
