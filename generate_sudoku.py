def generate_sudoku():
    board = initialize_board()
    solve_sudoku(board)
    remove_numbers(board)
    return board