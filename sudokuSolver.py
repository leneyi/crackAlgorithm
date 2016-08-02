
def sudokuSolver(self,board):
    if len(board) == 0 or board is None:
        return;
    self.solve(board);
    
def solve(self, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
               for c in '123456789':              
                 if self.isValid(board,i,j,c):
                     board[i][j] =c;
                     if self.solve(board):
                         return True;
                     else:
                         board[i][j] ='.';
               return False;
    return True;

def isValid(self, board, i,j, c):
    # check each row
    for row in range(0,9):
        if board[row][j] == c:
            return False;

    # check each column
    for col in range(0,9):
        if board[i][col] == c:
            return False;

    # check each block
    for row in range((i/3)*3, (i/3)*3+3):
        for col in range((j/3)*3, (j/3)*3+3):
            if board[row][col] == c:
                return False;
    return True;
