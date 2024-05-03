def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return board

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return board
            board[row][col] = 0  # Backtrack
    return None
