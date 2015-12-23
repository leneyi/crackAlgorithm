
def rotate(matrix):
    # the basic idea is to assign matrix[i][j] to matrix [j][len-1-i]
    leng = len(matrix);
    if leng == 0:
        return;
    for i in range(0,(leng+1)/2):
      for j in range(0,leng/2):
          temp = matrix[i][j];
          matrix[i][j] = matrix[leng-1-j][i];
          matrix[leng-1-j][i] = matrix[leng-1-i][leng-1-j];
          matrix[leng-1-i][leng-1-j] = matrix[j][leng-1-i];
          matrix[j][leng-1-i] = temp;
    return matrix;
    

print(rotate([[1,2],[3,4]]));
