def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens_util(board, col):
    # Base case: If all queens are placed
    if col >= len(board):
        return True

    # Try placing this queen in all rows of the current column
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            if solve_queens_util(board, col + 1):
                return True

            # If placing queen in the current position doesn't lead to a solution,
            # backtrack and try placing it in a different row
            board[i][col] = 0

    # If no row is found to place the queen, return False
    return False

def solve_queens(n):
    board = [[0] * n for _ in range(n)]

    if not solve_queens_util(board, 0):
        print("No solution exists.")
        return

    print("Solution:")
    for row in board:
        print(row)

# Example usage for 8-Queens
solve_queens(8)
