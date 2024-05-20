class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return f"{self.u} {self.v}"

    def __lt__(self, other):
        return self.w < other.w


M, K = map(int, input().split())
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edge = Edge(u, v, w)
    edges.append(edge)

edges.sort()

edges_update = edges[:K]
edges_update = edges_update[::-1]

for edge in edges_update:
    print(edge)
