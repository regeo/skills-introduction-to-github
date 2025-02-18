import random

def create_board(rows, cols):
    """Creates a game board (list of lists) with specified dimensions.

    Args:
        rows: The number of rows.
        cols: The number of columns.

    Returns:
        A list of lists representing the game board.  Each element is initially None.
    """
    return [[None for _ in range(cols)] for _ in range(rows)]



def print_board(board):
    """Prints the game board to the console.

    Args:
        board: The game board (list of lists).
    """
    for row in board:
        print(" | ".join(str(cell) if cell is not None else " " for cell in row))  # Nicer formatting
        print("-" * (4 * len(row) + 1))  # Separator lines



def is_valid_move(board, row, col):
    """Checks if a move is valid (within bounds and cell is empty).

    Args:
        board: The game board.
        row: The row index of the move.
        col: The column index of the move.

    Returns:
        True if the move is valid, False otherwise.
    """
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0  # Handle empty board case
    return 0 <= row < rows and 0 <= col < cols and board[row][col] is None



def make_move(board, row, col, player):
    """Makes a move on the board.  Assumes the move is valid (you should check first).

    Args:
        board: The game board.
        row: The row index of the move.
        col: The column index of the move.
        player: The player making the move (e.g., "X" or "O").
    """
    board[row][col] = player



def check_win(board, player):
    """Checks if the given player has won the game (horizontally, vertically, or diagonally).

    Args:
        board: The game board.
        player: The player to check for a win.

    Returns:
        True if the player has won, False otherwise.
    """
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    # Check horizontal
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check vertical
    for col in range(cols):
        if all(board[row][col] == player for row in range(rows)):
            return True

    # Check diagonals
    if rows == cols: # Only check diagonals if it's a square board
        if all(board[i][i] == player for i in range(rows)):
            return True
        if all(board[i][cols - 1 - i] == player for i in range(rows)):
            return True

    return False


def is_board_full(board):
    """Checks if the board is completely full (no more moves possible).

    Args:
        board: The game board.

    Returns:
        True if the board is full, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True


# Example usage (Tic-Tac-Toe):
rows = 3
cols = 3
board = create_board(rows, cols)
current_player = "X"

while True:
    print_board(board)
    try:
        row = int(input(f"Player {current_player}, enter row (0-{rows - 1}): "))
        col = int(input(f"Player {current_player}, enter column (0-{cols - 1}): "))

        if is_valid_move(board, row, col):
            make_move(board, row, col, current_player)

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"  # Switch players
        else:
            print("Invalid move. Try again.")
    except (ValueError, IndexError):  # Handle bad input
        print("Invalid input. Please enter numbers within the valid range.")
