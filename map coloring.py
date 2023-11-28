def is_valid_assignment(adjacency, assignment, node, color):
    for neighbor in adjacency[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking_coloring(adjacency, colors, assignment, node):
    if node not in adjacency:
        return assignment  # Base case: all nodes are assigned

    if node not in assignment:
        for color in colors:
            if is_valid_assignment(adjacency, assignment, node, color):
                assignment[node] = color
                result = backtracking_coloring(adjacency, colors, assignment, next_node(adjacency, assignment))
                if result is not None:
                    return result
                del assignment[node]

def next_node(adjacency, assignment):
    for next_node in adjacency:
        if next_node not in assignment:
            return next_node

def map_coloring(adjacency, colors):
    return backtracking_coloring(adjacency, colors, {}, next_node(adjacency, {}))

if __name__ == "__main__":
    # Example usage:
    adjacency = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW']
    }

    colors = ['Red', 'Green', 'Blue']

    result = map_coloring(adjacency, colors)

    if result is not None:
        print("Map Coloring Result:")
        for node, color in result.items():
            print(f"{node}: {color}")
    else:
        print("No valid coloring found.")
