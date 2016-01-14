
def canJump(nums):
    maxi = 0;
    for i in range(0,len(nums)):
         if i > maxi:
             return False;
         maxi = max(maxi, i+nums[i]);
    return True;

print(canJump([3,2,1,0,4]));
