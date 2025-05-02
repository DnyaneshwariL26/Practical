import heapq
#heapq is used to implement a priority queue
#for selecting the most promising node during traversal.
class Graph:
    def __init__(self):
        self.graph = {}#Stores nodes and their edges with costs.
        self.heuristic = {}# Stores heuristic values for nodes

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))  # Assuming an undirected graph

    def set_heuristic(self, node, value):
        self.heuristic[node] = value

    def a_star_search(self, start, goal):
        priority_queue = [(0 + self.heuristic[start], 0, start, [])]
        visited = set()

        while priority_queue:
            estimated_cost, cost, node, path = heapq.heappop(priority_queue)

            if node in visited:
                continue
            visited.add(node)
            path = path + [node]

            if node == goal:
                return path, cost

            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost + self.heuristic.get(neighbor, 0), 
                                                    cost + edge_cost, neighbor, path))

        return None, float('inf')

# User input to construct the graph
graph = Graph()
edges = int(input("Enter number of edges: "))

print("Enter edges (node1 node2 cost):")
for _ in range(edges):
    u, v, cost = input().split()
    graph.add_edge(u, v, int(cost))

heuristic_nodes = int(input("Enter number of heuristic values: "))
print("Enter heuristic values (node value):")
for _ in range(heuristic_nodes):
    node, value = input().split()
    graph.set_heuristic(node, int(value))

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

path, total_cost = graph.a_star_search(start_node, goal_node)

if path:
    print(f"Optimal path: {path}")
    print(f"Total cost: {total_cost}")
else:
    print("No path found.")
