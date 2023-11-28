import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from the start node to the current node
        self.h = h  # Heuristic estimate from the current node to the goal
        self.f = g + h  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar_8puzzle(start, goal):
    open_set = [PuzzleNode(start, None, 0, manhattan_distance(start, goal))]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor in get_neighbors_8puzzle(current_node.state):
            if neighbor in closed_set:
                continue

            g = current_node.g + 1  # Assuming a cost of 1 to move between states
            h = manhattan_distance(neighbor, goal)
            f = g + h
            new_node = PuzzleNode(neighbor, current_node, g, h)

            if not any(node.f < f and node.state == neighbor for node in open_set):
                heapq.heappush(open_set, new_node)

    return None  # No path found

def get_neighbors_8puzzle(state):
    # Given a state of the 8-puzzle, return possible neighboring states
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)

    # Possible moves: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))

    return neighbors

def manhattan_distance(state, goal):
    # Calculate the Manhattan distance heuristic for the 8-puzzle
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i * 3 + j]
            if value != 0:
                goal_position = divmod(goal.index(value), 3)
                distance += abs(i - goal_position[0]) + abs(j - goal_position[1])

    return distance

# Example usage:
start_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution_path = astar_8puzzle(start_state, goal_state)

if solution_path:
    print("Solution Path:")
    for state in solution_path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:])
        print()
else:
    print("No solution found.")
