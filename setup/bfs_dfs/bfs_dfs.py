from collections import deque
#The deque from collections is used as a queue to implement BFS efficiently.

class Graph:
    def __init__(self):
        self.graph = {}#A dictionary storing an Adjacency List representation of the graph.

    def add_edge(self, u, v): #Adds edges between two nodes u and v
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since it's an undirected graph

    def dfs_recursive(self, node, visited, result):
        #Starts from node, marks it as visited, and adds to result.
        #Recursively visits unvisited adjacent nodes.
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in self.graph.get(node, []):
                self.dfs_recursive(neighbor, visited, result)

    def bfs(self, start):#Starts from start, marks as visited, and processes all neighbors level-wise.
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.graph.get(node, []))

        return result

    def perform_searches(self, start):#Calls both DFS and BFS functions and prints results.
        dfs_result = []
        self.dfs_recursive(start, set(), dfs_result)
        bfs_result = self.bfs(start)

        print(f"Depth First Search (DFS) starting from {start}: {dfs_result}")
        print(f"Breadth First Search (BFS) starting from {start}: {bfs_result}")

# Taking user input to construct the graph
graph = Graph()
edges = int(input("Enter number of edges: "))


#This program is useful for network traversal, shortest path algorithms, and connected components detection in graph theory.

print("Enter edges (node1 node2):")
for _ in range(edges):
    u, v = input().split()
    graph.add_edge(u, v)

start_node = input("Enter the starting node for search: ")
graph.perform_searches(start_node)
