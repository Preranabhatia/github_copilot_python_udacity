import random

SIZE = 9

def is_valid(board, row, col, num):
    """Check if placing a number is valid according to Sudoku rules."""
    for i in range(SIZE):
        if board[row][i] == num or board[i][col] == num:
            return False
            
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_empty(board):
    """Find the next empty cell (represented by 0)."""
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_board(board):
    """Solve the board using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    numbers = list(range(1, 10))
    random.shuffle(numbers)

    for num in numbers:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_board(board):
                return True
            board[row][col] = 0
    return False

def count_solutions(board, limit=2):
    """Count the number of valid solutions to ensure uniqueness."""
    empty = find_empty(board)
    if not empty:
        return 1

    row, col = empty
    count = 0
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            count += count_solutions(board, limit)
            board[row][col] = 0
            if count >= limit:
                return count
    return count

def generate_puzzle(clues=35):
    """Generate a puzzle with exactly one unique solution."""
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    solve_board(board)
    solution = [row[:] for row in board]

    cells_to_remove = 81 - clues
    positions = [(r, c) for r in range(SIZE) for c in range(SIZE)]
    random.shuffle(positions)

    for row, col in positions:
        if cells_to_remove == 0:
            break
        
        temp = board[row][col]
        board[row][col] = 0
        
        # Test if unique solution remains
        test_board = [row[:] for row in board]
        if count_solutions(test_board) != 1:
            board[row][col] = temp
        else:
            cells_to_remove -= 1

    return board, solution