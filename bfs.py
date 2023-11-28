from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=' ')
            visited.add(current_node)
            queue.extend(graph[current_node])

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

    print("BFS traversal starting from node 'A':")
    bfs(g.graph, 'A')
