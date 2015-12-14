### suggestion, to avoid LTE, rewrite with Java is fine.
def numSquares(n):
    numsSquares = (n+1)*[0];
    i = 1;
    while(i<n+1):
        j =1;
        minN = n;
        while(j*j<=i):
          minN = min(minN,numsSquares[i-j*j]+1);
          j +=1;
        numsSquares[i] = minN;

        i +=1;
    return numsSquares[n];

print(numSquares(188));
