#Given an array and a value, remove all instances of that
#value in place and return the new length.
def removeElement(nums,val):
    currPos = 0;
    rightPos = 0;
    while currPos < len(nums):
        if not nums[currPos] == val:
            nums[rightPos] = nums[currPos];
            rightPos +=1;
        currPos +=1;

    return rightPos;


print(removeElement([1,2,4,4],4));
