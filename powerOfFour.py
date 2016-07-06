
def powerOfFour(n):
    print  n&(n-1) == 0 and n & 0x55555555 == n;
    return n&(n-1) == 0 and n & 0x55555555 == n;
powerOfFour(64);

