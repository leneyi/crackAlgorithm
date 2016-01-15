def uniquePaths(m,n):
    dp = [[0 for i in range(0,n)]for j in range(0,m)];
    for i in range(0,m):
        for j in range(0,n):
           if (i ==0 or j ==0):
               dp[i][j] = 1;
           else:
               dp[i][j] = dp[i-1][j]+ dp[i][j-1];
    return dp[m-1][n-1];
print(uniquePaths(9,2));
