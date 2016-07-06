
def powerOfTwo(n):
    if n <= 0:
        print False;
        return False;
    if n&(n-1) == 0:
        print True;
        return True;
    print False;
    return False;
powerOfTwo(64);

