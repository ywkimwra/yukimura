class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __lt__(self, other):
        if self.u < other.u:
            return True
        elif self.u == other.u and self.v < other.v:
            return True
        return False

    def __str__(self):
        s = f"{self.u} {self.v}"
        return s


def read_graph():
    N = int(input())
    adjacency_matrix = []

    for _ in range(N):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)

    edges = []

    for i in range(N):
        for j in range(i + 1, N):
            if adjacency_matrix[i][j] == 1:
                edges.append(Edge(i, j))

    edges.sort()
    return N, edges


def main():
    N, edges = read_graph()
    print(len(edges))
    for edge in edges:
        print(edge)

main()
