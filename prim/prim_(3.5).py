import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Since it's an undirected graph

    def prim_mst(self, start):
        min_heap = [(0, start)]  # (weight, vertex)
        visited = set()
        mst = []
        total_cost = 0

        while len(visited) < len(self.graph):
            weight, u = heapq.heappop(min_heap)

            if u in visited:
                continue

            visited.add(u)
            total_cost += weight

            for neighbor, edge_weight in self.graph.get(u, []):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
                    mst.append((u, neighbor, edge_weight))

        return mst, total_cost

# User input for graph construction
graph = Graph()
edges = int(input("Enter number of edges: "))

print("Enter edges (node1 node2 weight):")
for _ in range(edges):
    u, v, weight = input().split()
    graph.add_edge(u, v, int(weight))

start_node = input("Enter the starting node (alphabetical): ")
mst, total_cost = graph.prim_mst(start_node)

print("\nMinimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
print(f"\nTotal Cost of MST: {total_cost}")
