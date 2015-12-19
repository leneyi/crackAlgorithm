
def equi(A):
    sumA = 0;
    sumL =0;
    sumR =0;
    temp =0;
    for i in range(0,len(A)):
        sumA +=A[i];
    for i in range(0,len(A)):
        temp +=A[i];
        sumL = temp-A[i];
        sumR = sumA -temp;
        if sumL == sumR:
            return i;
    return -1;
print(equi([500,1,-2,2,-1]));
