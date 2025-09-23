def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="␣")
            if board[i][j] == 0:
                print(".", end="␣")
            else:
                print(board[i][j], end="␣")
    print ()

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
def is_valid(board, num, pos):
    return None

def solve_sudoku(board, row, col):
    empty_cell = find_empty(board) # This gets the empty cell

    if row == 8 and col == 9:
        return True
    
    if col == 9:
        row += 1
        col = 0
    
    if board[row][col] != 0:
        return solve_sudoku(board, row, col + 1)
    
    for num in range(1, 10):
        if is_valid(board, num, empty_cell)
    
    
    

sudoku_board = [
    [0, 1, 3, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 5, 2, 0, 0, 4, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 0, 0, 0, 0, 6, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 4, 0, 0, 0, 0],
    [7, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
]

solve_sudoku(sudoku_board, 0, 0)
