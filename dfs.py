class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', ['B', 'C'])
    g.add_edge('B', ['A', 'D', 'E'])
    g.add_edge('C', ['A', 'F', 'G'])
    g.add_edge('D', ['B'])
    g.add_edge('E', ['B', 'H'])
    g.add_edge('F', ['C'])
    g.add_edge('G', ['C'])
    g.add_edge('H', ['E'])

    visited_nodes = set()

    print("DFS traversal starting from node 'A':")
    dfs(g.graph, 'A', visited_nodes)
