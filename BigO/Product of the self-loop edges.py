class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

M = int(input())

edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edge = Edge(u, v, w)
    edges.append(edge)

special_edge = 0
product_weights = 1

for edge in edges:
    if edge.u == edge.v:
        special_edge += 1
        product_weights *= edge.w

product_weights = product_weights % (10**6 + 7)

if special_edge > 0:
    print(f"{special_edge} {product_weights}")
else:
    print(-1)