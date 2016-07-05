
def validSquare(n):
    low = 1;
    high = n;
    while low <= high:
        mid = low + (high -low)/2;
        if mid*mid == n:
            return True;
        if mid*mid < n:
            low = mid+1;
        if mid*mid >n :
            high = mid-1;
    return False;
validSquare(1000);
            
              
     
