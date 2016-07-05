
def getSum(a,b):
    if a == 0:
       return b;
    if b == 0:
       return a;
    while (b!=0):
        carry = a & b;
        sumi = a ^ b;
        a = sumi;
        b = carry << 1;
    print (a);
    return a;
getSum(402,50);
