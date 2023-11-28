class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2
    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2
    def __hash__(self):
        return hash((self.jug1, self.jug2))
    def __str__(self):
        return f"({self.jug1}, {self.jug2})"
def water_jug_dfs(capacity_jug1, capacity_jug2, target):
    initial_state = State(0, 0)
    visited = set()
    stack = [(initial_state, [])]
    while stack:
        current_state, path = stack.pop()
        if current_state in visited:
            continue
        visited.add(current_state)
        if current_state.jug1 == target or current_state.jug2 == target:
            path.append(current_state)
            return path
        next_states = get_next_states(current_state, capacity_jug1, capacity_jug2)
        for next_state, action in next_states:
            stack.append((next_state, path + [action]))
    return None
def get_next_states(current_state, capacity_jug1, capacity_jug2):
    next_states = []
    # Fill jug1
    next_state = State(capacity_jug1, current_state.jug2)
    next_states.append((next_state, f"Fill jug1"))
    # Fill jug2
    next_state = State(current_state.jug1, capacity_jug2)
    next_states.append((next_state, f"Fill jug2"))
    # Empty jug1
    next_state = State(0, current_state.jug2)
    next_states.append((next_state, f"Empty jug1"))
    # Empty jug2
    next_state = State(current_state.jug1, 0)
    next_states.append((next_state, f"Empty jug2"))
    # Pour jug1 to jug2
    pour_amount = min(current_state.jug1, capacity_jug2 - current_state.jug2)
    next_state = State(current_state.jug1 - pour_amount, current_state.jug2 + pour_amount)
    next_states.append((next_state, f"Pour jug1 to jug2"))
    # Pour jug2 to jug1
    pour_amount = min(current_state.jug2, capacity_jug1 - current_state.jug1)
    next_state = State(current_state.jug1 + pour_amount, current_state.jug2 - pour_amount)
    next_states.append((next_state, f"Pour jug2 to jug1"))
    return next_states
def main():
    capacity_jug1 = int(input("Enter the capacity of jug1: "))
    capacity_jug2 = int(input("Enter the capacity of jug2: "))
    target_amount = int(input("Enter the target amount: "))
    solution = water_jug_dfs(capacity_jug1, capacity_jug2, target_amount)
    if solution:
        print("Solution found:")
        for state, action in zip(solution, solution[1:]):
            print(f"{action}: {state}")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
