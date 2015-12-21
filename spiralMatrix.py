
def spiralMatrix(S):
    if len(S) == 0:
       return [];
    top = 0;
    bottom = len(S)-1;
    left = 0;
    right = len(S[0])-1;
    res = [];
    
    while (top <= bottom and left <= right):
        for i in range(left, right+1):
            res.append(S[top][i]);
        top +=1;
        for i in range(top,bottom+1):
            res.append(S[i][right]);
        right -=1;
        if (top <= bottom):
           for i in range(right,left -1,-1):
               res.append(S[bottom][i]);
        bottom -=1;

        if(left <= right):
            for i in range(bottom,top -1,-1):
                res.append(S[i][left]);
        left +=1;
    return res;

print (spiralMatrix([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]));
