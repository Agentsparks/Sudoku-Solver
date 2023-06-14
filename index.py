board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]



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
    c1 = False
    c2 = False
    for x in board[row]:
        if x == value:
            return False
        else:
            c1 = True
    for x in range(len(board)):
        if board[x][col] == value:
            return False
        else:
            c2 = True
    if c1 and c2:
        return True


print_board(board)
print(find_zero(board))
print(is_valid(board, 1,1,8))

def solve(board):
    zero = find_zero(board)
    i = zero[0]
    j = zero[1]
    if zero == None:
        return board
    for x in range(1,10):
        if is_valid(board,i,j,x):
            board[i][j] = x
            # print(x)
            solution = solve(board)
            if solution is not None:
                return solution
            board[i][j] = 0
        return None
print(solve(board))