

def minDistance(word1, word2):
    #edge case
    if len(word1) == 0 and len(word2) ==0:
       return 0;
    m = len(word1);
    n = len(word2);

    matrix = [[0 for col in range(0,n+1)]for row in range(0,m+1)];

    for i in range(0,m+1):
         matrix[i][0] = i;
    for i in range(0,n+1):
         matrix[0][i] = i;
    for i in range(1,m+1):
        for j in range(1,n+1):
          if word1[i-1] == word2[j-1]:
              matrix[i][j] = matrix[i-1][j-1];
          else:
   
 #             matrix[i][j] = min(matrix[i-i][j-1]+1,matrix[i][j-1]+1,matrix[i-1][j]+1);
              matrix[i][j] = min(matrix[i-1][j-1]+1, matrix[i-1][j]+1, matrix[i][j-1]+1);
              print matrix[i][j];
    return matrix[m][n];
        
         
    
print(minDistance('abcdef','akk'));
