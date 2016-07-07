
def integerBreak(n):
    # we need to consider the factor of 2 and 3
    # 2*(f-2)>f when f>4 so we can break any factor bigger than 4;

    if n == 1:
       return 1;
    if n == 2:
       return 1;
    if n == 3:
       return 2;
    res = 1;
    while (n>4):
        res *=3;
        n -=3;
    res *=n;
    print res;
    return res;
integerBreak(23);
