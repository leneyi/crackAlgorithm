
def moveZeroes(nums):
    rightPos = 0;
    currPos = 0;
    while currPos < len(nums):
        while currPos < len(nums) -1 and nums[currPos] == 0:
            currPos +=1;
        nums[rightPos] = nums[currPos];
        rightPos +=1;
        currPos +=1;
    while rightPos < len(nums):
        nums[rightPos] = 0;
        rightPos +=1;
#    print nums;

moveZeroes([0,0,0,0,9]);
