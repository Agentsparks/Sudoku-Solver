# Sudoku-Solver  

Desc: Can solve any Sudoku given a Sudoku in a Matrix
Matrix: A list of lists. In this case with a Sudoku board, the matrix is 9 lists of 9 elements each. 


How it works:
Functions: Print_Board(), Find_Zero(), Is_Valid(), Solve()

Print_Board(board): given a matrix, it returns a cleaner sudoku board.

Find_Zero(board): given a sudoku matrix, it returns the coordinates of the very first zero seen in the matrix in a list. [row,col]

Is_Valid(board, row, col, value): given a sudoku matrix, a numerical value, and the row and column of that given value, a boolean is retured which determines if the 
placement of the numerical value is legal in the current state of the sudoku board.

Solve(board): Given a board, recursion and backtracking is used to solve the sudoku board. Using the Find Zero() function, the AI searches for the first zero, and tries every value on it. For every value, 
it checks if that value is valid on those coordinates using the Is_Valid() function. If it isn't valid, the loops moves to the next value.  If it is, then it sets that value to that very position and recurses 
solve(board) again. However, if none of the values work, then the AI utilises backtracking, which sets that value back to zero and so on so forth until a better value is discovered in a previous state of the 
sudoku board. If the entire board is solved, then the board is returned in the print_board() function.
