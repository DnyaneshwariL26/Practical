import heapq#The heapq module is used to implement a priority queue,

class Graph:
    def __init__(self):
        self.graph = {}#self.graph is a dictionary representing an adjacency list,

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Assuming an undirected graph

    def dijkstra(self, start):
        priority_queue = [(0, start)]
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        #Initializes the priority queue with (0, start), meaning the distance to the start node is zero
        #distances dictionary stores the shortest known distance to each node.
        #Initially, distances are set to infinity (float('inf')), except for the start node (0).

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)#heapq.heappop(priority_queue) → Removes and returns the smallest element from the priority queue.

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# User input for graph construction
graph = Graph()
edges = int(input("Enter number of edges: "))

print("Enter edges (node1 node2 weight):")
for _ in range(edges):
    u, v, weight = input().split()
    graph.add_edge(u, v, int(weight))

start_node = input("Enter the start node: ")
shortest_paths = graph.dijkstra(start_node)

print(f"Shortest paths from {start_node}:")
for node, distance in shortest_paths.items():
    print(f"{node}: {distance}")
