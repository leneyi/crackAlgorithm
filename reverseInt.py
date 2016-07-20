
def reverseInt(x):
    sign = 1;
    if x < 0:
        sign = -1;
        x = -x;
    res = 0;
    while x>0:
        temp = x%10;
        res = res*10 + temp;
        x = x/10;
    if res > 2**31:
        print 0;
        return 0;
    if sign  == -1:
        print -res;
        return -res;
    print res;
    return res;

reverseInt(-89933);

        
