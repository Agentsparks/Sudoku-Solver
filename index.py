import time


empty_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]


board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]


board2 = [[7, 0, 9, 6, 8, 4, 0, 0, 0],
[0, 3, 0, 2, 0, 0, 0, 0, 8],
[0, 6, 8, 1, 3, 0, 2, 7, 0],
[2, 0, 6, 5, 4, 8, 0, 0, 1],
[0, 0, 1, 3, 0, 2, 0, 0, 5],
[5, 0, 0, 0, 0, 0, 7, 8, 2],
[3, 5, 2, 0, 0, 0, 8, 9, 4],
[0, 0, 4, 8, 0, 9, 3, 0, 7],
[0, 0, 0, 0, 2, 3, 0, 0, 6],]


def print_board(board):
    for x in board:
        spaces = ''
        for y in x:
            spaces += str(y) + ' '
        print(spaces)
        
def find_zero(board):
    for i, x in enumerate(board):
        for j, y in enumerate(x):
            if y == 0:
                return([i,j])
def is_valid(board,row,col,value):
    for x in board[row]:
        if x == value:
            return False
    for x in range(len(board)):
        if board[x][col] == value:
            return False
    square_row = row // 3
    square_col = col // 3
    for i in range(3):
        for j in range(3):
            if board[square_row*3 + i][square_col*3 + j] == value:
                return False
    return True


def solve(board):
    zero = find_zero(board)
    if zero == None:
        return board
    for x in range(1,10):
        if is_valid(board,zero[0],zero[1],x):
            board[zero[0]][zero[1]] = x
            solution = solve(board)
            if solution is not None:
                return solution
            board[zero[0]][zero[1]] = 0
    return None
print_board(empty_board)
print('-----------------------------------')
print_board(solve(empty_board))