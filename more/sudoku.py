def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j

def valid(board, num, pos):
    for i in range(len(board)):  # Check row
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):  # Check column
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3  # Check box
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

sudoku = [
    [9, 0, 6, 0, 8, 7, 0, 5, 0],
    [0, 8, 3, 6, 0, 9, 7, 0, 2],
    [2, 0, 0, 5, 4, 3, 0, 9, 8],
    [0, 6, 5, 4, 0, 2, 0, 7, 9],
    [7, 2, 0, 9, 6, 0, 4, 8, 0],
    [4, 3, 9, 0, 7, 0, 5, 2, 0],
    [0, 7, 0, 3, 2, 4, 9, 0, 5],
    [3, 0, 0, 8, 5, 0, 2, 6, 7],
    [0, 5, 2, 7, 0, 6, 8, 3, 0]
]

print_sudoku(sudoku)
solve(sudoku)
print("\n","solved:")
print_sudoku(sudoku)
