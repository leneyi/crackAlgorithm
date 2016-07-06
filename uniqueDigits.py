
def uniqueDigits(n):
    # when n = 1, res = 10;
    #      n = 2, res = 9*9
    #      n = 3, res = 9*9*8
    #      n = 4, res = 9*9*8*7
    #      n = 5, res = 9*9*8*7*6
    if n == 0:
        return 0;
    if n == 1 :
        return 10;
    temp = 9*9;
    i = 2;
    sumi = 10;
    n = min(10, n);
    while i<=n:
        sumi += temp
        temp *= (10-i)
        i +=1;
    print sumi;
    return sumi;
uniqueDigits(5);
        
