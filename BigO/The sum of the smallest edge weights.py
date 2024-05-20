class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def sum_of_smallest_edge_weights(M):
    edges = []

    for _ in range(M):
        u, v, w = map(int, input().split())
        edge = Edge(u, v, w)
        edges.append(edge)

    min_weight = 10**3
    for edge in edges:
        min_weight = min(min_weight, edge.w)

    total_sum = 0
    for edge in edges:
        if edge.w == min_weight:
            total_sum += edge.w

    return total_sum

M = int(input())
print(sum_of_smallest_edge_weights(M))