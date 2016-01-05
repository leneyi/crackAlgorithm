def zigzag(matrix):
    if matrix is None :
        return None;
    m = len(matrix);
    n = len(matrix[0]);
 
    # i+j = k, there are k element in the result
    res = [];

    for k in range(0,m+n-1):
        temp = [];
        if k<= n-1:
            i =0;
            j = k;
        else:
            j = n-1;
            i = k-j;
        while i<m and j>=0:
            temp.append(matrix[i][j]);
            i +=1;
            j -=1;
        res.append(temp);
    return res;
            


print(zigzag([[1,2],[5,6]]));
