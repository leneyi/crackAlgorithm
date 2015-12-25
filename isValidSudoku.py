
def isValidSudoku(self, board):
    curr = set();
    for i in range(0,9):
        for j in range(0,9):
            if not board[i][j]=='.':
               ele = board[i][j];
            if (i,ele) in curr or (ele,j) in curr or (i/3,j/3,ele) in curr:
               return False;
            else:
               curr.add((i,ele));
               curr.add((ele,j));
               curr.add((i/3,j/3,ele));
    return True;


