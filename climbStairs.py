def climbStairs(n):
# f(n) = f(n-1)+f(n-2)
    if (n ==0 or n ==1 or n ==2):
        return n;
    table = [0]*n;
    table[0]= 1;
    table[1] = 2;
    for n in range(2,n):
        table[n] = table[n-1]+table[n-2];
    return table[n-1];
        

