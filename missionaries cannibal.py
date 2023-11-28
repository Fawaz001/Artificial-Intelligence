from queue import Queue

def is_valid_state(state):
    # Check if the state is a valid state
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right = state

    # Check if missionaries outnumbered by cannibals on the left
    if missionaries_left < cannibals_left > 0 and missionaries_left != 0:
        return False

    # Check if missionaries outnumbered by cannibals on the right
    if missionaries_right < cannibals_right > 0 and missionaries_right != 0:
        return False

    return True

def generate_next_states(current_state):
    # Generate possible next states from the current state
    next_states = []
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right = current_state

    for move_missionaries in range(3):
        for move_cannibals in range(3):
            if 0 < move_missionaries + move_cannibals <= 2:
                next_state = (
                    missionaries_left - move_missionaries,
                    cannibals_left - move_cannibals,
                    not boat_left,
                    missionaries_right + move_missionaries,
                    cannibals_right + move_cannibals
                )

                if (
                    0 <= next_state[0] <= 3 and
                    0 <= next_state[1] <= 3 and
                    0 <= next_state[3] <= 3 and
                    0 <= next_state[4] <= 3 and
                    is_valid_state(next_state)
                ):
                    next_states.append(next_state)

    return next_states

def solve_missionaries_cannibals():
    initial_state = (3, 3, True, 0, 0)  # Initial state: (missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right)
    goal_state = (0, 0, False, 3, 3)  # Goal state: (missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right)

    visited_states = set()
    q = Queue()
    q.put((initial_state, []))  # Each item in the queue is a tuple (state, path)

    while not q.empty():
        current_state, path = q.get()
        visited_states.add(current_state)

        if current_state == goal_state:
            return path + [current_state]

        next_states = generate_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited_states:
                q.put((next_state, path + [current_state]))

    return None

def print_solution(solution):
    if solution:
        for i, state in enumerate(solution):
            print(f"Step {i + 1}: {state}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    solution_path = solve_missionaries_cannibals()
    print_solution(solution_path)
