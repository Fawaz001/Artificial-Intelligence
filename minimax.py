def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def evaluate(board):
    # Check rows
    for row in board:
        if all(cell == 'X' for cell in row):
            return 10
        elif all(cell == 'O' for cell in row):
            return -10

    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 10
        elif all(board[row][col] == 'O' for row in range(3)):
            return -10

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 10
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return -10

    return 0  # No winner

def is_moves_left(board):
    return any(cell == '_' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    elif not is_moves_left(board):
        return 0

    if is_maximizing:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = '_'
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = '_'
        return best

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = '_'

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

if __name__ == "__main__":
    # Example usage for a Tic-Tac-Toe game
    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['_', '_', '_']
    ]

    print("Current Board:")
    print_board(board)

    best_move = find_best_move(board)

    if best_move != (-1, -1):
        print(f"Best Move: {best_move}")
        board[best_move[0]][best_move[1]] = 'X'
        print("Updated Board:")
        print_board(board)
    else:
        print("No valid moves left.")
