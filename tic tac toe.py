def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows
    if any(all(cell == player for cell in row) for row in board):
        return True

    # Check columns
    if any(all(board[row][col] == player for row in range(3)) for col in range(3)):
        return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def get_player_move(player):
    while True:
        try:
            row = int(input(f"Enter row (1-3) for Player {player}: ")) - 1
            col = int(input(f"Enter column (1-3) for Player {player}: ")) - 1

            if is_valid_move(board, row, col):
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row, col = get_player_move(current_player)
        board[row][col] = current_player

        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'
