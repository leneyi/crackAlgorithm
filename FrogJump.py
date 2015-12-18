'''
- A bug is trying to cross the river start from position 0 to position X
- Every time bug can jump no more than the D steps (1 to D steps);
- Leaves will fall from the tree to the river based on schedule A. A[0] = 1 
means a leaf will fall on position 1 at time 0;
- Need to find the earliest time that the bug can jump from position 0 to x 
using leaves; If there is no answer, return -1;

Example:
A = [1, 3, 1, 4, 2, 5]
X = 7 
D = 3

Answer: 3
Explanation: At time 3, there will be leaves on position 1,3, and 4; bug can
jump 1 step, 3 step, and then 3 steps to cross the river;

Expected time complexity is O(n)
'''

def FrogJump(A,X,D):
    if(A is None or len(A) == 0 or X<=D):
       return 0;
    result = [X]*(X+1);
    result[0] =0;
    dict = {};
    dict[0] =0;
    dict[X] =0;

    for i in range(0,len(A)):
        if(not A[i] in dict):
            dict[A[i]] =i;

    for j in range(1,X+1):
        if(j in dict):
            if(j<=D):
                result[j] =dict[j];
            else:
               for m in range(1,D+1):
                 if dict[j]<result[j-m]:
                    result[j] = min(result[j],result[j-m]);
                 else:
                    result[j] = min(result[j],dict[j]);
        
            
    return -1 if result[X]==X else result[X];

A = [1,3,1,4,2,5];
#print A[0];
print(FrogJump(A,7,3));
